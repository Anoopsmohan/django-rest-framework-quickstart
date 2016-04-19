__author__ = 'anoop.sm'

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from snippet4 import views


urlpatterns = [
    url(r'^$', views.SnippetList.as_view()),
    url(r'(?P<pk>[0-9]+)/$', views.SnippetList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
