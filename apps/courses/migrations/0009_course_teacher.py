# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-10 17:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import organization.models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_teacher_image'),
        ('courses', '0008_lesson_lesson_times'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(null=organization.models.Teacher, on_delete=django.db.models.deletion.CASCADE, to='organization.Teacher', verbose_name='\u8bb2\u5e08'),
        ),
    ]