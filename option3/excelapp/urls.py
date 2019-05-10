from django.conf.urls import patterns, url
from .views import home, get_file, all_files, excel_table

urlpatterns = patterns('',
	url(r'^$',home, name='home'),
	url(r'^upload-file/$',get_file, name='get_file'),
	url(r'^all-files/$',all_files, name='all_files'),
    url(r'^excel-table/(?P<id>\d+)/$',excel_table, name='excel_table'),   
)