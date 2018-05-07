from django import forms
from .models import *

class SalariesForm(forms.ModelForm):

    class Meta:
        model = Salaries
        fields = ('emp_no', 'salary', 'from_date', 'to_date')

