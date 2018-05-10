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
    url(r'^employee_profile/(?P<pk>\d+)/salary_new/$', views.salary_new ,name='salary_new'),
    url(r'^employee_profile/(?P<pk>\d+)/employee_new/$', views.deptemp_new ,name='deptemp_new'),
    url(r'^employee_profile/(?P<pk>\d+)/manager_new/$', views.manager_new ,name='manager_new'),
    url(r'^employee_profile/(?P<pk>\d+)/position_new/$', views.title_new ,name='title_new'),
    url(r'^employee_new', views.employee_new ,name='employee_new'),
 ]