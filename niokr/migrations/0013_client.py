# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-14 17:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('niokr', '0012_auto_20160214_2153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, null=True, verbose_name='\u0418\u043c\u044f')),
                ('last_name', models.CharField(max_length=50, null=True, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f')),
                ('organization', models.CharField(max_length=50, null=True, verbose_name='\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f')),
                ('position', models.CharField(max_length=50, null=True, verbose_name='\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c')),
                ('phone_number', models.CharField(max_length=50, null=True, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('address', models.CharField(max_length=150, null=True, verbose_name='\u0410\u0434\u0440\u0435\u0441\u0441')),
            ],
        ),
    ]
