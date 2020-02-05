from django.urls import re_path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import index


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

app_name = 'simple'
urlpatterns = [
    # Examples:
    # url(r'^$', 'examples.views.home', name='home'),
    # url(r'^examples/', include('examples.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    re_path(r'', index)
]

urlpatterns += staticfiles_urlpatterns()
