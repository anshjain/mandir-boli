# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget

from django.contrib import admin

from account.models import Account
from mandir.constants import SPECIAL_MSG, VIDHAN_CON
from mandir.models import Mandir, Record, MandirImage, BoliChoice, VratDetail
from mandir.utils import send_normal_sms


class MandirResource(resources.ModelResource):

    class Meta:
        model = Mandir
        exclude = ('created',)


class MandirAdmin(ImportExportModelAdmin):
    list_display = ('name', 'contract_number', 'bank_name', 'account_number',
                    'account_name', 'ifsc_code', 'branch')
    resource_class = MandirResource

    def get_queryset(self, request):
        """Limit records to those that belong to the user temple."""

        qs = super(MandirAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            # It is mine, all mine. Just return everything.
            return qs
        # Now we just add an extra filter on the queryset and
        # we're done. Assumption: Page.owner is a foreignkey
        # to a User.
        return qs.filter(id=request.user.userprofile.mandir.id)


class RecordResource(resources.ModelResource):

    mandir = fields.Field(column_name='mandir', attribute='mandir', widget=ForeignKeyWidget(Mandir, 'name'))
    title = fields.Field(column_name='title', attribute='title', widget=ForeignKeyWidget(BoliChoice, 'name'))
    pan_card = fields.Field(column_name='pan_card', attribute='account', widget=ForeignKeyWidget(Account, 'pan_card'))
    account = fields.Field(column_name='phone_number', attribute='account', widget=ForeignKeyWidget(Account, 'phone_number'))
    paid = Field()

    def dehydrate_paid(self, record):
        return 'Paid' if record.paid else 'Not Paid'

    def dehydrate_description(self, record):
        return record.account.description

    class Meta:
        model = Record
        export_order = ('id', 'mandir', 'account', 'description', 'pan_card', 'title', 'amount', 'boli_date', 'paid')
        exclude = ('created', 'transaction_id', 'payment_date')


class RecordAdmin(ImportExportModelAdmin):
    list_display_links = ('get_title',)
    search_fields = ('account__description', 'account__phone_number',)
    resource_class = RecordResource
    list_per_page = 15
    actions = ['make_paid', 'make_as_unpaid', 'Send_sms']

    def make_paid(self, request, queryset):
        rows_updated = queryset.update(paid=True, payment_date=datetime.now(),
                                       description='Admin user {} update this record and marked it paid'.format(request.user.username))
        if rows_updated == 1:
            message_bit = "1 record was"
        else:
            message_bit = "%s records were" % rows_updated
        self.message_user(request, "%s successfully marked as paid." % message_bit)
    make_paid.short_description = "Mark selected records as paid"

    def make_as_unpaid(self, request, queryset):
        rows_updated = queryset.update(paid=False, payment_date=datetime.now(),
                                       description='Admin user {} update this record and marked it as unpaid'.format(request.user.username))
        if rows_updated == 1:
            message_bit = "1 record was"
        else:
            message_bit = "%s records were" % rows_updated
        self.message_user(request, "%s successfully marked as unpaid." % message_bit)
    make_as_unpaid.short_description = "Mark selected records as unpaid"

    def Send_sms(self, request, queryset):
        """
        Send sms to selected records
        """
        records = queryset.all()
        for record in records:
            if record.title.name in ('indra', 'indrani', 'indra - indrani'):
                send_normal_sms(record.account.phone_number, message=SPECIAL_MSG, sender='SHRSJM')
            else:
                send_normal_sms(record.account.phone_number, sender='SHRSJM')
        self.message_user(request, "Send reminder SMS successfully.")

    Send_sms.short_description = "Send reminder SMS to selected records"

    def get_names(self, obj):
        if obj.account.description:
            return obj.account.description
        else:
            name = obj.description.split('\n')[0]
            return name

    get_names.short_description = 'Name'

    def get_account_no(self, obj):
        return obj.account.phone_number
    get_account_no.short_description = 'Phone Number'

    def get_title(self, obj):
        return obj.title.name
    get_title.short_description = 'Title'

    def get_readonly_fields(self, request, obj=None):
        """
        Admin can update the account details where as sub admin can't.
        """
        if not request.user.is_superuser:
            return ('account', 'mandir')
        return []

    def get_pan_card(self, obj):
        return obj.account.pan_card
    get_pan_card.short_description = 'PAN Card'

    def get_list_filter(self, request):
        """
        Update list filter and display list based on logged in admin users.
        """
        if request.user.is_superuser:
            return 'paid', 'boli_date', 'mandir', 'title', 'request_by_user', 'remaining_amt'
        else:
            return 'paid', 'boli_date', 'title', 'request_by_user', 'remaining_amt'

    def get_list_display(self, request):
        """
        Update list filter and display list based on logged in admin users.
        """
        list_display = ['paid', 'get_title', 'get_names', 'get_account_no', 'amount', 'boli_date',
                        'payment_date', 'transaction_id', 'get_pan_card', 'request_by_user']
        if request.user.is_superuser:
            return ['mandir'] + list_display
        else:
            return list_display

    def get_queryset(self, request):
        """Limit records to those that belong to the user temple."""

        qs = super(RecordAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            # It is mine, all mine. Just return everything.
            return qs.order_by('-boli_date')
        # Now we just add an extra filter on the queryset and
        # we're done. Assumption: Page.owner is a foreignkey
        # to a User.
        return qs.filter(mandir=request.user.userprofile.mandir).order_by('-boli_date')


class MandirImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_mandir_name', 'event_url', )

    def get_mandir_name(self, obj):
        return obj.mandir.name
    get_mandir_name.short_description = 'Mandir Name'

    def get_queryset(self, request):
        """Limit records to those that belong to the user temple."""

        qs = super(MandirImageAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            # It is mine, all mine. Just return everything.
            return qs
        # Now we just add an extra filter on the queryset and
        # we're done. Assumption: Page.owner is a foreignkey
        # to a User.
        return qs.filter(mandir=request.user.userprofile.mandir)


class BoliChoiceResource(resources.ModelResource):

    class Meta:
        model = BoliChoice
        exclude = ('created',)


class BoliChoiceAdmin(ImportExportModelAdmin):
    list_display = ('name', 'request_choice')
    resource_class = BoliChoiceResource


class VratDetailResource(resources.ModelResource):

    class Meta:
        model = VratDetail
        exclude = ('created',)


class VratDetailAdmin(ImportExportModelAdmin):
    list_display = ('name', 'enabled', 'vrat_date')
    resource_class = VratDetailResource


admin.site.register(Mandir, MandirAdmin)
admin.site.register(Record, RecordAdmin)
admin.site.register(MandirImage, MandirImageAdmin)
admin.site.register(BoliChoice, BoliChoiceAdmin)
admin.site.register(VratDetail, VratDetailAdmin)
