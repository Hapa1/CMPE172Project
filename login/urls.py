from django.conf.urls import url
from django.conf.urls import include
from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^dashboard', views.dashboard),
    url(r'^', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^', include('social_django.urls', namespace='social')),

    #url(r'^login/auth0$',views.index, name='index')

]