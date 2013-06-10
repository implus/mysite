from django.conf.urls import *
from views import hello, current_datetime, hours_ahead,display_meta
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/',include(admin.site.urls)),
    (r'^hello/$', hello),
    (r'^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    (r'^lx/',display_meta),
)

urlpatterns += patterns('books.views',
    (r'^search/$','search'),
)

urlpatterns += patterns('contact.views',
    (r'^contact/$','contact'),
    (r'^contact/thanks/$','thanks'),
)
