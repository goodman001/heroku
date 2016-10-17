"""Heroku URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from userLogin import views as userLogin_views # import userLogin
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', userLogin_views.index, name = "home"),
    url(r'^register/$', userLogin_views.register, name = "register"),
    url(r'^api/v1/users/$',userLogin_views.api,name = "api"),
    url(r'^api/v1/users/(\d+)/$',userLogin_views.api1,name = "api1"),
    url(r'^api/v1/users/(\d+)/(entry)/$',userLogin_views.api2,name = "api2"),
    url(r'^api/v1/users/(\d+)/(entry)/(\d+)/$',userLogin_views.api3,name = "api3"),
    url(r'^api/v1/users/(\d+)/(create)/$',userLogin_views.api4,name = "api4"),
]
