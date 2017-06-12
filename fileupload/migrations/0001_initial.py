# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-09 05:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
