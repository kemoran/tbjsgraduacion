# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import TbjsGraduacion.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nombres', models.CharField(max_length=255)),
                ('apellidos', models.CharField(max_length=255)),
                ('correo_electronico', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=10, null=True, blank=True)),
            ],
            options={
                'db_table': 'alumnos',
            },
        ),
        migrations.CreateModel(
            name='Asesores',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('correo_electronico', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=10, null=True, blank=True)),
                ('user', models.OneToOneField(related_name='asesor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'asesores',
            },
        ),
        migrations.CreateModel(
            name='Carreras',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('carrera', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'carreras',
            },
        ),
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('comentario', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'comentarios',
            },
        ),
        migrations.CreateModel(
            name='Empresas',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=255)),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=10)),
                ('encargado', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'empresas',
            },
        ),
        migrations.CreateModel(
            name='Etapas',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('etapa', models.CharField(max_length=100)),
                ('archivo', TbjsGraduacion.models.FileInputPersonalizado(null=True, upload_to='archivos', blank=True)),
                ('fecha_aprovachon', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'etapas',
            },
        ),
        migrations.CreateModel(
            name='Perfiles',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('perfil', models.CharField(max_length=2)),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'perfiles',
            },
        ),
        migrations.CreateModel(
            name='TiposTrabajos',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('tipo', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'tipos_trabajos',
            },
        ),
        migrations.CreateModel(
            name='TrabajosGraduacion',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=45)),
                ('comentario', models.TextField(null=True, blank=True)),
                ('alumnos_1_id', models.ForeignKey(related_name='alumnos_1_id', db_column='alumnos_1_id', to='TbjsGraduacion.Alumnos')),
                ('alumnos_2_id', models.ForeignKey(related_name='alumnos_2_id', db_column='alumnos_3_id', blank=True, to='TbjsGraduacion.Alumnos', null=True)),
                ('alumnos_3_id', models.ForeignKey(related_name='alumnos_3_id', db_column='alumnos_2_id', blank=True, to='TbjsGraduacion.Alumnos', null=True)),
                ('asesores_id', models.ForeignKey(to='TbjsGraduacion.Asesores', db_column='asesores_id')),
                ('empresas_id', models.ForeignKey(to='TbjsGraduacion.Empresas', db_column='empresas_id')),
                ('tipos_trabajos_id', models.ForeignKey(to='TbjsGraduacion.TiposTrabajos', db_column='tipos_trabajos_id')),
            ],
            options={
                'db_table': 'trabajos_graduacion',
            },
        ),
        migrations.AddField(
            model_name='etapas',
            name='trabajos_graduacion_id',
            field=models.ForeignKey(to='TbjsGraduacion.TrabajosGraduacion', db_column='trabajos_graduacion_id'),
        ),
        migrations.AddField(
            model_name='comentarios',
            name='etapas_id',
            field=models.ForeignKey(to='TbjsGraduacion.Etapas', db_column='etapas_id'),
        ),
        migrations.AddField(
            model_name='alumnos',
            name='carreras_id',
            field=models.ForeignKey(to='TbjsGraduacion.Carreras', db_column='carreras_id'),
        ),
        migrations.AddField(
            model_name='alumnos',
            name='user',
            field=models.OneToOneField(related_name='alumno', to=settings.AUTH_USER_MODEL),
        ),
    ]
