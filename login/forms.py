from django import forms
from users.models import *

class NewEmployeeForm(forms.ModelForm):

    class Meta:
        model = Employees
        fields = ('first_name', 'last_name', 'birth_date', 'gender', 'hire_date')

class SalariesForm(forms.ModelForm):

    class Meta:
        model = Salary
        fields = ('salary', 'from_date', 'to_date')

class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Departments
        fields = ('dept_id',)

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = DeptEmp
        fields = ('dept_id', 'from_date', 'to_date')

class ManagerForm(forms.ModelForm):

    class Meta:
        model = DeptManager
        fields = ('dept_id', 'from_date', 'to_date')

class TitleForm(forms.ModelForm):

    class Meta:
        model = Titles
        fields = ('title', 'from_date', 'to_date')
