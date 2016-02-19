# -- coding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

Fields = (
    ('Обработка Материалов', u'Обработка Материалов'),
    ('Строительство', u'Строительство'),
    ('Энергообеспечение', u'Энергообеспечение'),
    ('IT', u'IT'),
    ('Приборостроение', u'Приборостроение'),
    ('Экология', u'Экология'),
)
# Create your models here.

class Client(models.Model):
	first_name = models.CharField(verbose_name=u'Имя', max_length=50, null=True)
	last_name = models.CharField(verbose_name=u'Фамилия', max_length=50, null=True)
	organization = models.CharField(verbose_name=u'Организация', max_length=50, null=True)
	position = models.CharField(verbose_name=u'Должность', max_length=50, null=True)
	phone_number = models.CharField(verbose_name=u'Номер телефона', max_length=50, null=True)
	email = models.EmailField(null=True)
	address = models.CharField(verbose_name=u'Адрес', max_length=150, null=True)
	def __unicode__(self):
		return self.first_name + ' ' + self.last_name

class Research_interests(models.Model):
    name = models.CharField(max_length=50, choices=Fields)
    description = models.TextField()
    def __unicode__(self):
        return self.name

class Expert(AbstractUser):
    research_interests = models.ForeignKey(Research_interests, null=True, blank=True, verbose_name=u'Область')  
    phone_number = models.CharField(verbose_name=u'Номер личного телефона', max_length=50, null=True)
    work_phone_number = models.CharField(verbose_name=u'Номер рабочего телефона', max_length=50, null=True)
    def __unicode__(self):
    	return self.first_name + ' ' + self.last_name + ' ' + ', ' + self.research_interests.name

class Request(models.Model):
	client = models.ForeignKey(Client, null=True, blank=True, verbose_name=u'Заказчик', related_name='client')
	research_interests = models.ForeignKey(Research_interests, null=True, verbose_name=u'Область')
	title = models.CharField(verbose_name=u'Заголовок', max_length=50, null=True)
	description = models.TextField(verbose_name=u'Описание', null=True)
	is_assigned = models.BooleanField(verbose_name=u'Назначена', default=False)
	expert = models.ForeignKey(Expert, null=True, blank=True, verbose_name=u'Закрепленный эксперт')
	def __unicode__(self):
		return self.client.organization