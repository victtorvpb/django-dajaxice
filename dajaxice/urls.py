try:
    from django.urls import re_path
except ImportError:
    from django.conf.urls.defaults import url as re_path


from .views import DajaxiceRequest

urlpatterns = [
    re_path(r'^(.+)/$', DajaxiceRequest.as_view(), name='dajaxice-call-endpoint'),
    re_path(r'', DajaxiceRequest.as_view(), name='dajaxice-endpoint')
]
