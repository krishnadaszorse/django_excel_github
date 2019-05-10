from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator
from django.conf import settings
from .forms import ExcelFileForm
from .models import ExcelFile, ExcelFileData, ExcelData
from .excel import get_excel_data, sort_data

def home(request):
	variables = {}
	return render_to_response('index.html', variables)

def get_file(request):
	form = ExcelFileForm()
	if request.method == 'POST':
		form = ExcelFileForm(request.POST,request.FILES)
		if form.is_valid():
			excel_file = form.save(commit=False)
			excel_file.file_name = request.FILES['attachment'].name
			excel_file.save()
			datas=get_excel_data(str(settings.BASE_DIR)+str(excel_file.attachment.url))
			count=1
			for data in datas:
				excel_file_data=ExcelFileData()
				excel_file_data.excel_file=excel_file
				excel_file_data.priority=count
				excel_file_data.save()
				count1=1
				for key,value in data:
					excel_data=ExcelData()
					excel_data.excel_file_data=excel_file_data
					excel_data.heading=key
					excel_data.value=value
					excel_data.priority=count1
					excel_data.save()
					count1=count1+1
				count=count+1

	variables = RequestContext(request, {
        'form':form,
    })
	return render_to_response('excel_forms.html', variables)

def all_files(request):
	excel_files_all=ExcelFile.objects.all()
	paginator = Paginator(excel_files_all, 25)
	page = request.GET.get('page') if request.GET.has_key('page') else 1
	excel_files = paginator.page(page)
	variables = {
	'excel_files':excel_files,
	}
	return render_to_response('excel_list.html', variables)

def excel_table(request, id):
	excel_file=ExcelFile.objects.get(id=id)
	excel_file_data_all=ExcelFileData.objects.filter(excel_file=excel_file)
	if request.GET.has_key('sort'):
		excel_file_data_all=sorted(ExcelFileData.objects.filter(excel_file=excel_file), key=lambda x: sort_data(x,request.GET.get('sort')))
	headings = excel_file_data_all[0].exceldata_set.all()
	paginator = Paginator(excel_file_data_all, 25)
	page = request.GET.get('page') if request.GET.has_key('page') else 1
	excel_file_data = paginator.page(page)
	variables = {
	'excel_file':excel_file,
	'headings':headings,
	'excel_file_data':excel_file_data,
	}
	return render_to_response('excel_table.html', variables)

