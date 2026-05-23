"""Boli URL Configuration"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, re_path as url, path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView

from events.views import EventListView, EventCreateView
from mandir.views import (RecordListView, EntryCreateView, ajax_single_account, contact,
                          AboutView, payment_complete, HomeView, ReturnView, RaiseBoliCreateView)
from mandir.jain_calendar_views import (
    jain_calendar_index, jain_reminders, jain_save_reminders,
    jain_notifications_today, jain_search,
)

admin.site.site_header = 'PunyaUday Fund'
admin.site.site_title = 'PunyaUday Fund admin'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', LoginView.as_view(template_name='login.html'), name="login"),
    url(r'^accounts/logout/$', LogoutView.as_view(template_name='base.html'), name="logout"),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^search/$', RecordListView.as_view(), name='record-list'),
    url(r'^add/$', EntryCreateView.as_view(), name='add-record'),
    url(r'^raise-request/$', RaiseBoliCreateView.as_view(), name='raise-request'),
    url(r'^get/description/$', ajax_single_account, name='des-search'),
    url(r'^about-us/$', AboutView.as_view(), name='about'),
    url(r'^return/$', ReturnView.as_view(), name='return'),
    url(r'^contact-us/$', contact, name='contact-us'),
    url(r'^payment/done/$', payment_complete, name='payment-done'),
    url(r'^events/(?P<event_id>\d+)/$', EventListView.as_view(), name='event'),
    url(r'^event/registration/$', EventCreateView.as_view(), name='event-registration'),
    path('captcha/', include('captcha.urls')),
    # Jain Calendar URLs
    path('jain-calendar/', jain_calendar_index, name='jain-calendar'),
    path('jain-calendar/reminders/', jain_reminders, name='jain-reminders'),
    path('jain-calendar/reminders/save/', jain_save_reminders, name='jain-save-reminders'),
    path('jain-calendar/notifications/today/', jain_notifications_today, name='jain-notifications-today'),
    path('jain-calendar/search/', jain_search, name='jain-search'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
