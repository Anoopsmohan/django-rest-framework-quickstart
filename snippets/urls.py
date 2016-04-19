__author__ = 'anoop.sm'

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views_1


urlpatterns = [
    url(r'^$', views_1.snippet_list),
    url(r'(?P<pk>[0-9]+)/$', views_1.snippet_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)
