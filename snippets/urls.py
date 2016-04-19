__author__ = 'anoop.sm'

from django.conf.urls import url

from snippets import views_1


urlpatterns = [
    url(r'^$', views_1.snippet_list),
    url(r'(?P<pk>[0-9]+)/$', views_1.snippet_detail)
]

