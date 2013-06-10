from django.conf.urls import *
from views import hello, current_datetime, hours_ahead,display_meta

import books.views
import contact.views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/',include(admin.site.urls)),
    (r'^hello/$', hello),
    (r'^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    (r'^lx/',display_meta),
    #(r'^search-form/$', views.search_form),
    (r'^search/$',books.views.search),
    (r'^contact/$',contact.views.contact),
    (r'^contact/thanks/$',contact.views.thanks),
)

