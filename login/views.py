from django.shortcuts import *
from django.contrib.auth.decorators import login_required
from users.models import *
from login.models import *
from django.views.generic import *
from django.template.context_processors import csrf
from django.shortcuts import render_to_response
from login.forms import *

import json


# Create your views here.
def index(request):
    template_name = 'login/index.html'
    return render(request,template_name)

@login_required
def dashboard(request):
    users = Employees.objects.order_by('last_name')
    user = request.user
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
        search_id = (request.POST['search_id'])
    else:
        search_text_first = ''
        search_text_last = ''     
        search_id = ''
    employee_list = Employees.objects.order_by('last_name')

    for employee in employee_list:
        employee.first_name = employee.first_name.lower()

    employees_lower =  employee_list.filter(first_name__contains=search_text_first) & employee_list.filter(last_name__contains=search_text_last) & employee_list.filter(emp_id__contains=search_id)    
    top10 = employees_lower[:20]
    
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
    depts_details = DeptEmp.objects.filter(emp_id=profile.emp_id)
    managers = DeptManager.objects.filter(emp_id=profile.emp_id)
    titles = Titles.objects.filter(emp_id=profile.emp_id)
    salaries = Salary.objects.filter(emp_id=profile.emp_id).order_by('-from_date')
    return render_to_response('login/employee_profile.html', {
        'salaries': salaries, 
        'profile' : profile,
        'depts_details' : depts_details,
        'managers': managers,
        'titles':titles,

        })

def salary_new(request, pk):
    user = get_object_or_404(Employees, pk=pk)
    if request.method == "POST":
        form = SalariesForm(request.POST)
        if form.is_valid():
            salaries = form.save(commit=False)
            salaries.emp_id = user;
            salaries.save()
            return redirect('profile', pk=user.pk)
    else:
        form = SalariesForm()
    return render(request, 'login/salary_new.html', {'form': form})

def employee_new(request):
    if request.method == "POST":
        form = NewEmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            last = Employees.objects.lastes
            count = Employees.objects.count()+1
            employee.emp_id = count
            employee.save()
            emp_id = count
            return redirect('profile', pk=emp_id)
    else:
        form = NewEmployeeForm()
    return render(request, 'login/salary_new.html', {'form': form})

def deptemp_new(request, pk):
    user = get_object_or_404(Employees, pk=pk)
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.emp_id = user;
            employee.save()
            return redirect('profile', pk=user.pk)
    else:
        form = EmployeeForm()
    return render(request, 'login/salary_new.html', {'form': form})

def manager_new(request, pk):
    user = get_object_or_404(Employees, pk=pk)
    if request.method == "POST":
        form = ManagerForm(request.POST)
        if form.is_valid():
            manager = form.save(commit=False)
            manager.emp_id = user;
            manager.save()
            return redirect('profile', pk=user.pk)
    else:
        form = ManagerForm()
    return render(request, 'login/salary_new.html', {'form': form})

def title_new(request, pk):
    user = get_object_or_404(Employees, pk=pk)
    if request.method == "POST":
        form = TitleForm(request.POST)
        if form.is_valid():
            title = form.save(commit=False)
            title.emp_id = user;
            title.save()
            return redirect('profile', pk=user.pk)
    else:
        form = TitleForm()
    return render(request, 'login/salary_new.html', {'form': form})


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