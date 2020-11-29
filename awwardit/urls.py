"""awwardit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from awwards import views as app_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('awwards.urls')),
    url(r'^accounts/register',app_views.register_user,name='register_user' ),
    url(r'^accounts/login/$',app_views.user_login,name='user_login'),
    url(r'^logout/$', app_views.user_logout, name='user_logout'),
]
