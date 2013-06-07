from django.conf.urls.defaults import *
from mysite.views import hello, current_datetime, hours_ahead
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	(r'^admin/',include(admin.site.urls)),
    (r'^hello/$', hello),
    (r'^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
)
