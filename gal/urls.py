from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gal.views.home', name='home'),
    # url(r'^gal/', include('gal.foo.urls')),

    url(r'^$', 'gal.views.index'),
    url(r'^image/(.+)$', 'gal.views.view_image', name='view_image'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
