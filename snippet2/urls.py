__author__ = 'anoop.sm'

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from snippet2 import views


urlpatterns = [
    url(r'^$', views.snippet_list),
    url(r'(?P<pk>[0-9]+)/$', views.snippet_details)
]

urlpatterns = format_suffix_patterns(urlpatterns)
