# Create your views here.
from django.shortcuts import render_to_response 
from django.template import RequestContext
from plataforma.apps.home.forms import LoginForm
#clases de manejo de login 
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect

def index_view(request):
	return render_to_response('home/index.html', context_instance=RequestContext(request))

def login_view(request):
	mensaje = ""
	if request.user.is_authenticated():
		# para redireccionar se debe llamar a la vista 
		return HttpResponseRedirect('index')
	else:
		if request.method == "POST":
			form = LoginForm(request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				usuario = authenticate(username=username, password=password)
				if usuario is not None and usuario.is_active:
					login(request,usuario)
					return HttpResponseRedirect('index')
				else:
					mensaje = "usuario y/o password incorrecto"
		form = LoginForm()
		ctx = {'form':form, 'mensaje': mensaje}
	return render_to_response('home/login.html', ctx, context_instance=RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

