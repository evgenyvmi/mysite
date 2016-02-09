# This Python file uses the following encoding: utf-8
from django.forms import ModelForm
from niokr.models import Request
from niokr.models import Expert

class RequestForm(ModelForm):
	class Meta: 
		model = Request
		fields = '__all__'

class ExpertForm(ModelForm):
	class Meta:
		model = Expert
		fields = ['current_request_id']