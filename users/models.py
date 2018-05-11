from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Departments(models.Model):
    dept_id = models.CharField(primary_key=True, max_length=4)
    dept_name = models.CharField(unique=True, max_length=40)

    def __str__(self):
        return self.dept_name

class Dept(models.Model):
    dept_id = models.CharField(primary_key=True, max_length=4)
    dept_name = models.CharField(unique=True, max_length=40)

class DeptEmp(models.Model):
    deptemp_id = models.IntegerField(primary_key=True, default=False)
    emp_id = models.ForeignKey('Employees', models.DO_NOTHING, db_column='emp_id')
    dept_id = models.ForeignKey(Departments, models.DO_NOTHING, db_column='dept_id')
    from_date = models.DateField()
    to_date = models.DateField()

class DeptManager(models.Model):
    deptmanager_id = models.IntegerField(primary_key=True, default=False)
    emp_id = models.ForeignKey('Employees', models.DO_NOTHING, db_column='emp_id')
    dept_id = models.ForeignKey(Departments, models.DO_NOTHING, db_column='dept_id')
    from_date = models.DateField()
    to_date = models.DateField()

class Employees(models.Model):
    emp_id = models.IntegerField(primary_key=True, default=False)
    birth_date = models.DateField()
    first_name = models.CharField(max_length=14, blank=True)
    last_name = models.CharField(max_length=16, blank=True)
    gender = models.TextField(blank=True, max_length=1) 
    hire_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.first_name

class Salary(models.Model):
    salary_id = models.IntegerField(primary_key=True, default=False)
    emp_id= models.ForeignKey(Employees, on_delete=models.CASCADE)
    salary = models.IntegerField()
    from_date = models.DateField()
    to_date = models.DateField()

class Titles(models.Model):
    title_id = models.IntegerField(primary_key=True, default=False)
    emp_id = models.ForeignKey(Employees, models.DO_NOTHING, db_column='emp_id')
    title = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField(blank=True, null=True)

