from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'gal.views.home'),
    url(r'^(?P<gallery>[^/]+)/download$', 'gal.views.download_all'),
    url(r'^(?P<gallery>[^/]+)/image/(?P<filename>.+)$', 'gal.views.view_image', name='view_image'),
    url(r'^(?P<gallery>[^/]+)/thumb/(?P<filename>.+)$', 'gal.views.view_thumbnail', name='view_thumbnail'),
    url(r'^(?P<gallery>[^/]+)/pick/(?P<filename>.+)$', 'gal.views.pick', name='pick'),
    url(r'^(?P<gallery>[^/]+)/(?P<filename>.+)$', 'gal.views.image', name='image'),
    url(r'^(?P<gallery>[^/]+)$', 'gal.views.index'),
)
