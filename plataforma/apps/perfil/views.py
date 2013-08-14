from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from plataforma.apps.perfil.models import *

def vista_perfil(request):
	perfil = Perfil.objects.all()
	ctx = {'perfil':perfil}
	return render_to_response('perfil/perfil.html', ctx, context_instance=RequestContext(request))

def vista_completa(request, id_perfil):
	perf = Perfil.objects.get(id=id_perfil)
	ctx = {'perfil':perf}
	
	return render_to_response('perfil/mantenedorperfil.html', ctx, context_instance=RequestContext(request))
