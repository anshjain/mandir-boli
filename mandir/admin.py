# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field

from django.contrib import admin

from mandir.models import Mandir, Record, MandirImage, BoliChoice


class MandirAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'contract_number', 'email')

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

    mandir = Field()
    account = Field()
    title = Field()
    paid = Field()
    names = Field()

    def dehydrate_mandir(self, record):
        return record.mandir.name

    def dehydrate_names(self, record):
        return record.account.description

    def dehydrate_account(self, record):
        return record.account.phone_number

    def dehydrate_title(self, record):
        return record.title.name

    def dehydrate_paid(self, record):
        return 'Paid' if record.paid else 'Not Paid'

    class Meta:
        model = Record
        export_order = ('mandir', 'names', 'account', 'title', 'amount', 'boli_date', 'paid', 'description')
        exclude = ('created', 'transaction_id', 'payment_date', 'id')


class RecordAdmin(ImportExportModelAdmin):
    list_display_links = ('get_title',)
    search_fields = ('account__description', 'account__phone_number',)
    resource_class = RecordResource
    list_per_page = 15
    actions = ['make_paid', 'make_as_unpaid']

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

    def get_list_filter(self, request):
        """
        Update list filter and display list based on logged in admin users.
        """
        if request.user.is_superuser:
            return 'paid', 'boli_date', 'mandir'
        else:
            return 'paid', 'boli_date'

    def get_list_display(self, request):
        """
        Update list filter and display list based on logged in admin users.
        """
        list_display = ['paid', 'get_title', 'get_names', 'get_account_no', 'amount', 'boli_date',
                        'payment_date', 'transaction_id']
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


class BoliChoiceAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Mandir, MandirAdmin)
admin.site.register(Record, RecordAdmin)
admin.site.register(MandirImage, MandirImageAdmin)
admin.site.register(BoliChoice, BoliChoiceAdmin)
