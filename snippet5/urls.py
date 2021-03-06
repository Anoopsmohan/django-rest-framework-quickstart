__author__ = 'anoop.sm'

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from snippet5 import views


urlpatterns = [
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^$', views.SnippetList.as_view(), name='snippet-list'),
    url(r'(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(), name='snippet-detail'),
    url(r'^(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(), name='snippet-highlight')
]

urlpatterns = format_suffix_patterns(urlpatterns)
