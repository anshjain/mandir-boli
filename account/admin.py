# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from account.models import Account, UserProfile

from import_export import resources
from import_export.admin import ImportExportModelAdmin


class AccountResource(resources.ModelResource):

    class Meta:
        model = Account
        export_order = ('id', 'phone_number', 'description')
        exclude = ('created',)
        skip_unchanged = True
        report_skipped = True


class AccountAdmin(ImportExportModelAdmin):
    list_display = ('phone_number', 'description')
    search_fields = ('description', 'phone_number')
    list_per_page = 15
    resource_class = AccountResource


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_mandir_name')

    def get_mandir_name(self, obj):
        return obj.mandir.name
    get_mandir_name.short_description = 'Mandir Name'


admin.site.register(Account, AccountAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
