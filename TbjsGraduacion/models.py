# -*- encoding: utf-8 -*-
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

""" CAMPO PERSONALIZADO PARA FILEINPUT """
# FileField personalizado ----------------------------------------------------------------------------------------------------------------------------------------------------------
from django.db.models import FileField
from django.forms import forms
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
class FileInputPersonalizado(FileField):
	def __init__(self, content_types=None, max_upload_size=None, **kwargs):
		self.content_types = content_types
		self.max_upload_size = max_upload_size
		
		super(FileInputPersonalizado, self).__init__(**kwargs)
		
	def clean(self, *args, **kwargs):
		data = super(FileInputPersonalizado, self).clean(*args, **kwargs)

		file = data.file
		try:
			content_type = file.content_type
			if content_type in self.content_types:
				if file._size > self.max_upload_size:
					raise forms.ValidationError(_('Tamaño maximo soportado: %s. Tamaño actual del archivo %s') % (filesizeformat(self.max_upload_size), filesizeformat(file._size)))
			else:
				raise forms.ValidationError(_('Tipo de formato no soportado.'))
		except AttributeError:
			pass

		return data
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Carreras(models.Model):
	id = models.AutoField(primary_key=True)
	carrera = models.CharField(max_length=255)

	class Meta:
		db_table = 'carreras'


class TiposTrabajos(models.Model):
	id = models.AutoField(primary_key=True)
	tipo = models.CharField(max_length=50)

	class Meta:
		db_table = 'tipos_trabajos'


class Empresas(models.Model):
	id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=255)
	direccion = models.CharField(max_length=255)
	telefono = models.CharField(max_length=10)
	encargado = models.CharField(max_length=255)

	class Meta:
		db_table = 'empresas'


class Perfiles(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE) #request.user.profile.perfil 
	perfil = models.CharField(max_length=2)

	class Meta:
		db_table = 'perfiles'


class Alumnos(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.OneToOneField(User, related_name="alumno", on_delete=models.CASCADE)
	carreras_id = models.ForeignKey(Carreras, db_column='carreras_id', on_delete=models.CASCADE)
	nombres = models.CharField(max_length=255)
	apellidos = models.CharField(max_length=255)
	correo_electronico = models.CharField(max_length=255)
	telefono = models.CharField(max_length=10, blank=True, null=True)

	class Meta:
		db_table = 'alumnos'


class Asesores(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.OneToOneField(User, related_name="asesor", on_delete=models.CASCADE)
	nombre = models.CharField(max_length=100)
	correo_electronico = models.CharField(max_length=255)
	telefono = models.CharField(max_length=10, blank=True, null=True)

	class Meta:
		db_table = 'asesores'


class TrabajosGraduacion(models.Model):
	id = models.AutoField(primary_key=True)
	tipos_trabajos_id = models.ForeignKey(TiposTrabajos, db_column='tipos_trabajos_id', on_delete=models.CASCADE)
	empresas_id = models.ForeignKey(Empresas, db_column='empresas_id', on_delete=models.CASCADE)
	nombre = models.CharField(max_length=45)
	comentario = models.TextField(blank=True, null=True)
	asesores_id = models.ForeignKey(Asesores, db_column='asesores_id', on_delete=models.CASCADE)
	alumnos_1_id = models.ForeignKey(Alumnos, related_name='alumnos_1_id', db_column='alumnos_1_id', on_delete=models.CASCADE)
	alumnos_2_id = models.ForeignKey(Alumnos, related_name='alumnos_2_id', db_column='alumnos_3_id', on_delete=models.CASCADE, blank=True, null=True)
	alumnos_3_id = models.ForeignKey(Alumnos, related_name='alumnos_3_id', db_column='alumnos_2_id', on_delete=models.CASCADE, blank=True, null=True)

	class Meta:
		db_table = 'trabajos_graduacion'


class Etapas(models.Model):
	id = models.AutoField(primary_key=True)
	trabajos_graduacion_id = models.ForeignKey(TrabajosGraduacion, db_column='trabajos_graduacion_id', on_delete=models.CASCADE)
	etapa = models.CharField(max_length=100)
	archivo = FileInputPersonalizado(blank=True, null=True, upload_to='archivos', content_types=['application/pdf'], max_upload_size=429916160)
	fecha_aprovachon = models.DateTimeField(blank=True, null=True)

	class Meta:
		db_table = 'etapas'


class Comentarios(models.Model):
	id = models.AutoField(primary_key=True)
	etapas_id = models.ForeignKey(Etapas, db_column='etapas_id', on_delete=models.CASCADE)
	comentario = models.TextField(blank=True, null=True)

	class Meta:
		db_table = 'comentarios'