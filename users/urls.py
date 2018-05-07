from django.conf.urls import url, static
from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index')
    url(r'^salary/$', views.salaries_new, name='salaries_new'),
]