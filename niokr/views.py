# This Python file uses the following encoding: utf-8
from django.shortcuts import render
from .models import Request
from .models import Expert
from django.http import HttpResponseRedirect
from .forms import RequestForm
from django.contrib.auth import logout
from .forms import ExpertForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
# Create your views here.
def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return render(request, 'NIOKR/logout.html', {})
def post_list(request):
	return render(request, 'NIOKR/Главная страница.html', {})
def post_login(request):
	if request.POST:
		auth_form = AuthenticationForm()
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = authenticate(username=username, password=password)
		print user
		if user is not None:
			return HttpResponseRedirect('http://127.0.0.1:8000/expert/')
		else:
			return render(request, 'NIOKR/index.html', {'form': auth_form})
	else: 
		auth_form = AuthenticationForm()
		return render(request, 'NIOKR/index.html', {'form': auth_form})
#def post_request(request):
#	return render(request, 'NIOKR/Заявка.html', {})
def expert(request):
	print 'jkkljhkjhljhkih;jh;oj;ojloj;kj;kj;kjlkj'
	if request.POST:
		
		form = ExpertForm(request.POST)
		current_user = request.user
		print current_user.id

	else:		
		form = ExpertForm()

	return render(request, 'NIOKR/Эксперт.html', {'Expert': form})

def create_request(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RequestForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/')
        else:
        	return render(request, 'NIOKR/Заявка.html', {'form': form})
   			

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RequestForm()

	return render(request, 'NIOKR/Заявка.html', {'form': form})