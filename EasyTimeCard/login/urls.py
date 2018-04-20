from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    #url(r'^$',views.index, name='index'),
    url(r'$',login, {'template_name': 'login/index.html'}),
    url(r'$', views.index, {'next_page':'login: login'})
]