from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'smileapp.views.home', name='home'),
    # url(r'^smiles/', include('smiles.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)


# Serve static files when debug false
#if not settings.DEBUG:
urlpatterns += patterns('',
         (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
     )

urlpatterns += patterns('',
url(r'^(?P<page_name>\w+)$', 'smileapp.views.staticpage', name='home'),
)