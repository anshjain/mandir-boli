# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime, timedelta
from twilio.rest import Client
import simplejson as json

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.template.loader import get_template
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView

from account.models import Account

from mandir.models import Record
from mandir.forms import SearchForm, EntryForm, ContactForm, PaymentForm


class RecordListView(ListView):
    model = Record
    form_class = SearchForm
    context_object_name = 'records'
    template_name = 'records.html'

    def get_mandir_info(self):
        """
        Get the mandir info.
        """
        user = self.request.user
        if hasattr(user, 'userprofile'):
            profile = user.userprofile
            return profile.mandir if hasattr(profile, 'mandir') else None

    def get_context_data(self, *args, **kwargs):
        context = super(RecordListView, self).get_context_data(*args, **kwargs)

        phone_number = self.request.GET.get('phone_number')
        if phone_number:
            context.update({'phone_number': phone_number})

        context.update({'form': self.form_class(), 'mandir': self.get_mandir_info(), 'payment_form': PaymentForm()})

        return context

    def get_queryset(self):
        form = self.form_class(self.request.GET)

        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            return self.model.objects.filter(account__phone_number__icontains=phone_number, paid=False)

        # Default data will be displayed for two hours only after creation.
        mandir = self.get_mandir_info()
        time_threshold = datetime.now() - timedelta(hours=2)
        return self.model.objects.filter(boli_date__date=datetime.today(), boli_date__gt=time_threshold,
                                         mandir=mandir, paid=False)


@method_decorator(login_required, name='dispatch')
class EntryCreateView(LoginRequiredMixin, FormView):
    form_class = EntryForm
    model = Record
    template_name = 'entry.html'
    success_url = '/add/#entry'

    def get_context_data(self, *args, **kwargs):
        context = super(EntryCreateView, self).get_context_data(*args, **kwargs)

        # Mandir object into the context
        context['mandir'] = self.request.user.userprofile.mandir
        return context

    def form_valid(self, form):
        # check account present with phone number or not.
        account, created = Account.objects.get_or_create(
            phone_number=form.cleaned_data['phone_number'],
        )
        if created:
            account.description = form.cleaned_data['description']
            account.save()

        # hard code as of now
        mandir = self.request.user.userprofile.mandir
        amount = form.cleaned_data['amount']

        _, record_created = self.model.objects.get_or_create(
            mandir=mandir,
            account=account,
            title=form.cleaned_data['title'],
            description=form.cleaned_data['description'],
            amount=amount,
            boli_date=datetime.now()
        )
        if record_created:
            send_sms(account.phone_number, amount)
            messages.success(self.request, "Record added successfully !!")

        return super(EntryCreateView, self).form_valid(form)


def send_sms(phone_number, amount):
    """
        Will send an sms to end user.
    """
    if settings.ACCOUNT_SID:
        try:
            client = Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)
            sms_mgs = """Thanks to donate {}/- \n Mandir Committee is very thankful to you."""
            message = client.messages.create(
                body=sms_mgs.format(amount),
                from_=settings.TWILIO_USER,
                to='+91{}'.format(phone_number)
            )
        except Exception:
            pass


def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('message', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')

            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }

            content = template.render(context)

            email = EmailMessage(
                "Feedback submitted on Punya Unday Funds", content,
                "Punya Unday Funds", ['jain.scs@gmail.com'],
                headers={'Reply-To': contact_email}
            )

            email.send()
            messages.success(request, "Thank you for contacting us !!")
            return redirect('contact-us')
        else:
            form_class = form
            messages.success(request, "Please provide correct email address !!")

    mandir = request.user.userprofile.mandir if request.user.is_authenticated() else None
    return render(request, 'contact.html', {'form': form_class, 'mandir': mandir})


def payment_complete(request):
    form_class = PaymentForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            mod_pay = request.POST.get('payment_mode', '')
            send_to = [request.POST.get('send_to', '')]
            id_details = request.POST.get('id_details', '')
            record_id = request.POST.get('record_id')
            phone_number = request.POST.get('phone_number')

            # get record info
            record = Record.objects.get(id=record_id)

            # Email the profile with the
            # contact information
            template = get_template('payment_template.txt')

            name = record.account.description.split(',')[0]
            send_to.append(record.mandir.email)

            context = {
                'name': name,
                'mod_pay': mod_pay,
                'id_details': id_details,
                'amount': record.amount,
                'mandir_name': record.mandir.name,
            }

            content = template.render(context)
            send_to.extend(settings.ADMIN_EMAILS)

            # update record mark it as paid and store send email copy in description.
            record.description = content
            record.paid = True
            record.transaction_id = id_details if id_details else 'Cash'
            record.payment_date = datetime.now()
            record.save()

            email = EmailMessage(
                "Thanks for the Payment", content,
                "Punya Unday Funds", send_to
            )

            email.send()
            messages.success(request, "Thank you for contacting us !!")

    url = reverse('record-list') + "?phone_number={}#record".format(phone_number)
    return HttpResponseRedirect(url)


class AboutView(TemplateView):
    template_name = 'about_us.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)

        # Mandir object into the context
        if self.request.user.is_authenticated():
            context['mandir'] = self.request.user.userprofile.mandir

        return context


def ajax_single_account(request):
    '''gets single item'''
    if not request.is_ajax():
        return HttpResponse(json.dumps({'result': False}))

    # get slug from data
    phone_number = request.GET.get('phone_number', None)

    # get item from slug
    account = get_object_or_404(Account, phone_number=phone_number)
    return HttpResponse(json.dumps(
        {
            'result': True,
            'description': account.description,
        }))