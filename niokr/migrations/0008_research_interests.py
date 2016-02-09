# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-24 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('niokr', '0007_auto_20151225_0133'),
    ]

    operations = [
        migrations.CreateModel(
            name='Research_interests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430 \u041c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u043e\u0432', '\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430 \u041c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u043e\u0432'), ('\u0421\u0442\u0440\u043e\u0438\u0442\u0435\u043b\u044c\u0441\u0442\u0432\u043e', '\u0421\u0442\u0440\u043e\u0438\u0442\u0435\u043b\u044c\u0441\u0442\u0432\u043e'), ('\u042d\u043d\u0435\u0440\u0433\u043e\u043e\u0431\u0435\u0441\u043f\u0435\u0447\u0435\u043d\u0438\u0435', '\u042d\u043d\u0435\u0440\u0433\u043e\u043e\u0431\u0435\u0441\u043f\u0435\u0447\u0435\u043d\u0438\u0435'), ('IT', 'IT'), ('\u041f\u0440\u0438\u0431\u043e\u0440\u043e\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435', '\u041f\u0440\u0438\u0431\u043e\u0440\u043e\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435'), ('\u042d\u043a\u043e\u043b\u043e\u0433\u0438\u044f', '\u042d\u043a\u043e\u043b\u043e\u0433\u0438\u044f')], max_length=50)),
                ('short_description', models.TextField()),
            ],
        ),
    ]
