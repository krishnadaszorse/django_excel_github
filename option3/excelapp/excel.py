import xlrd

def get_excel_data(path):
	# Give the location of the file 
	loc = (path) 
  
	# To open Workbook 
	wb = xlrd.open_workbook(loc)
	sheet = wb.sheet_by_index(0)
	final_dict=[[(sheet.cell_value(0, y), sheet.cell_value(x, y)) for y in range(sheet.ncols)] for x in range(1, sheet.nrows)]
	return final_dict

def sort_data(data_list, heading):
	data_dict={ x.heading:x.value for x in data_list.exceldata_set.all()}
	return data_dict.get(heading)