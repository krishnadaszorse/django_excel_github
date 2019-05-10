from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError
import os

def validate_file_extension(value):
  ext = os.path.splitext(value.name)[1]
  valid_extensions = ['.xls','.xlsx','.xlsm']
  if not ext in valid_extensions:
    raise ValidationError(u'File not supported!')


class ExcelFile(models.Model):
	file_name = models.CharField(verbose_name=u'File name',max_length=100, null=True)
	attachment = models.FileField(verbose_name=u'Attachment', upload_to="uploads/attachments", validators=[validate_file_extension])
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.attachment

	class Meta:
		verbose_name = ("Excel File")
		verbose_name_plural = ("Excel Files")

class ExcelFileData(models.Model):
	excel_file = models.ForeignKey(ExcelFile)
	priority = models.IntegerField(verbose_name=u'Priority')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.heading

	class Meta:
		verbose_name = ("Excel File Data")
		verbose_name_plural = ("Excel File Datas")

class ExcelData(models.Model):
	excel_file_data = models.ForeignKey(ExcelFileData)
	heading = models.CharField(verbose_name=u'Heading',max_length=100, null=True)
	value = models.CharField(verbose_name=u'Value',max_length=100, null=True)
	priority = models.IntegerField(verbose_name=u'Priority')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.heading

	class Meta:
		verbose_name = ("Excel Data")
		verbose_name_plural = ("Excel Datas")
