# This Python file uses the following encoding: utf-8
from django.forms import ModelForm
from niokr.models import Request
from niokr.models import Expert
from niokr.models import Client


class RequestForm(ModelForm):
	class Meta: 
		model = Request
		fields = ['client', 'research_interests', 'description']

class ExpertForm(ModelForm):
	class Meta:
		model = Expert
		fields = '__all__'

class ClientForm(ModelForm):
	class Meta:
		model = Client
		fields = '__all__'

