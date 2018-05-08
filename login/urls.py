from django.conf.urls import url
from django.conf.urls import include
from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^dashboard', views.dashboard),
    url(r'^employees_list', views.employees_list),
    url(r'^', include('django.contrib.auth.urls', )),
    url(r'^', include('social_django.urls', )),
    url(r'^employee_profile/(?P<pk>\d+)/$', views.employee_profile ,name='profile'),
    url(r'^search', views.search_employees),
] 