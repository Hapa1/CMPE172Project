from users.models import *
from login.models import *
import datetime
from haystack import indexes

class EmployeeIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True,)
	content_auto = indexes.EdgeNgramField(model_attr='first_name')

	def get_model(self):
		return Employees

	def index_queryset(self, using=None):
		return self.get_model().objects.all()