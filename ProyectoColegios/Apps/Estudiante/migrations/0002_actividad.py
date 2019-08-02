# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-14 23:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MateriaGrado', '0001_initial'),
        ('Estudiante', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('idActividad', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('tituloActividad', models.CharField(max_length=70)),
                ('descripcionActividad', models.TextField(max_length=200)),
                ('estado', models.BooleanField()),
                ('rutaArchivo', models.FileField(blank=True, null=True, upload_to='Archivos/Actividad/')),
                ('calificacion', models.PositiveIntegerField(default=0)),
                ('foraneaEstudiante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Estudiante.Estudiante')),
                ('foraneaMateriaGrado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MateriaGrado.MateriaGrado')),
            ],
        ),
    ]
