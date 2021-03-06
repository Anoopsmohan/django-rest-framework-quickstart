"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from quickstart import views
from snippet5.views import api_root

#router = routers.DefaultRouter()
#router.register(r'user', views.UserViewSet)
#router.register(r'group', views.GroupViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^', include(router.urls)),
    url(r'^$', api_root),
    url(r'^snippets1/', include('snippet1.urls')),
    url(r'^snippets2/', include('snippet2.urls')),
    url(r'^snippets3/', include('snippet3.urls')),
    url(r'^snippets4/', include('snippet4.urls')),
    url(r'^snippets5/', include('snippet5.urls')),
    url(r'^snippets6/', include('snippet6.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
