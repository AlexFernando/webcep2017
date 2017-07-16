# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-13 01:01
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20170713_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='dni',
            field=models.CharField(error_messages={'invalid': 'El campo ingresado es inválido', 'required': 'Este campo es requerido'}, max_length=8, validators=[django.core.validators.RegexValidator('^\\d{8}$')]),
        ),
        migrations.AlterField(
            model_name='register',
            name='last_name',
            field=models.CharField(error_messages={'invalid': 'El campo ingresado es inválido', 'required': 'Este campo es requerido'}, max_length=200),
        ),
        migrations.AlterField(
            model_name='register',
            name='name',
            field=models.CharField(error_messages={'invalid': 'El campo ingresado es inválido', 'required': 'Este campo es requerido'}, max_length=200),
        ),
        migrations.AlterField(
            model_name='register',
            name='school_name',
            field=models.CharField(error_messages={'invalid': 'El campo ingresado es inválido', 'required': 'Este campo es requerido'}, max_length=200),
        ),
        migrations.AlterField(
            model_name='register',
            name='year_in_school',
            field=models.IntegerField(choices=[(0, 'Elige tu año escolar'), (1, '1ro'), (2, '2do'), (3, '3ro'), (4, '4to'), (5, '5to')], default=0, error_messages={'invalid': 'El campo ingresado es inválido', 'required': 'Este campo es requerido'}),
        ),
    ]