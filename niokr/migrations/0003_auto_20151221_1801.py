# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-21 13:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('niokr', '0002_auto_20151220_2106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='custumer_id',
        ),
        migrations.AddField(
            model_name='request',
            name='address',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='request',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='research_interests_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='niokr.Research_interests'),
        ),
        migrations.AlterField(
            model_name='request',
            name='short_description',
            field=models.TextField(null=True),
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
