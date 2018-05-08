from django.shortcuts import *
from django.contrib.auth.decorators import login_required
from users.models import *
from login.models import *
from django.views.generic import *
from django.template.context_processors import csrf
from django.shortcuts import render_to_response

import json


# Create your views here.
def index(request):
    template_name = 'login/index.html'
    return render(request,template_name)

@login_required
def dashboard(request):
    users = Employees.objects.order_by('last_name')
    #user = request.user
    #auth0user = user.social_auth.get(provider="auth0")
    
    args = {}
    args.update(csrf(request))

    args['employees'] = users

    #userdata = {
    #   'user_id': auth0user.uid,
    #    'name': user.first_name,
    #    'picture': auth0user.extra_data['picture']
    #}
    return render_to_response('login/dashboard.html', args)
    #return render(request, 'login/dashboard.html', args, {
    #    'auth0User': auth0user,
    #    'userdata': json.dumps(userdata, indent=4),
    #    'users' : users,
    #})

def search_employees(request):
    #E_list = SearchQuerySet().autocomplete(content_auto=request.POST.get('search_text', ''))
    #return render_to_response('ajax_search.html', {'Employees': E_list})

    if request.method == "POST":

        search_text_first = request.POST['search_text_first']
        search_text_last = request.POST['search_text_last']
        search_id = request.POST['search_id']
        
        
    else:
        search_text_first = ''
        search_text_last = ''
        search_id = ''
    
    employee_list = Employees.objects.order_by('last_name')

    for employee in employee_list:
        employee.first_name = employee.first_name.lower()

    employees_lower = employee_list.filter(first_name__contains=search_text_first) & employee_list.filter(last_name__contains=search_text_last)  & employee_list.filter(emp_id__contains=search_id)
    top10 = employees_lower[:10]
    
    return render_to_response('login/ajax_search.html',{
        'employees' : top10,
        'search_text_first' : search_text_first,
        'search_text_last' : search_text_last,

        },)

def employees_list(request):

    E_list = Employees.objects.order_by('emp_id')
    return render(request, 'login/employee_list.html', {'Employees': E_list})

def employee_profile(request, pk):
    profile = get_object_or_404(Employees, pk=pk)
    return render(request, 'login/employee_profile.html', {'profile' : profile})



class AccountList(ListView):
    model = Employees
    paginate_by = 12
    template_name = 'login/dashboard.html'
    context_object_name = 'accounts'

    def get_queryset(self):
        try:
            a = self.request.GET.get('account',)
        except KeyError:
            a = None
        if a:
            account_list = Account.objects.filter(
                name__icontains=a,
                owner=self.request.user
            )
        else:
            account_list = Account.objects.filter(owner=self.request.user)
        return account_list

    
    def dispatch(self, *args, **kwargs):
        return super(AccountList, self).dispatch(*args, **kwargs)