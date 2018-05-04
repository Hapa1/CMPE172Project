"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import include, url
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    #     url(r'^saml2_auth/', include('django_saml2_auth.urls')),
    #     url(r'^accounts/login/$', django_saml2_auth.views.signin),
    #     url(r'^admin/login/$', django_saml2_auth.views.signin),
    #
     url(r'^admin/', admin.site.urls),
     #url(r'^login/',include('login.urls')),
     url(r'^', include('login.urls')),
     url(r'^timecard/',include('timecard.urls')),
     #url(r'^login/auth0',include('login.urls')),



]
