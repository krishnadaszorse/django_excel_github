from django.forms import ModelForm
from .models import ExcelFile

class ExcelFileForm(ModelForm):
	class Meta:
		model = ExcelFile
		fields = ('attachment',)