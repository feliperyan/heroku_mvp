from django.conf.urls import patterns, include, url
import settings
from hello_app.views import *

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

from hello_app.admin import my_admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hello.views.home', name='home'),
    # url(r'^hello/', include('hello.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', include(my_admin.urls)),

    #url(r'^$', include(hello_app.urls)),
    url(r'^$', index),
    url(r'^thanks/', thanks, name='thanks'),
    url(r'^contact/$', contact, name='contact'),
)

#FELIPE: MUST CHANGE THIS!
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )