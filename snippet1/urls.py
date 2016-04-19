__author__ = 'anoop.sm'

from django.conf.urls import url

from snippet1 import views


urlpatterns = [
    url(r'^$', views.snippet_list),
    url(r'(?P<pk>[0-9]+)/$', views.snippet_detail)
]
