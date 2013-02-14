from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gal.views.home', name='home'),
    # url(r'^gal/', include('gal.foo.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^(?P<gallery>.+)/download$', 'gal.views.download_all'),
    url(r'^(?P<gallery>.+)/image/(?P<filename>.+)$', 'gal.views.view_image', name='view_image'),
    url(r'^(?P<gallery>.+)/thumb/(?P<filename>.+)$', 'gal.views.view_thumbnail', name='view_thumbnail'),
    url(r'^(?P<gallery>.+)/(?P<filename>.+)$', 'gal.views.image', name='image'),
    url(r'^(?P<gallery>.+)$', 'gal.views.index'),
)
