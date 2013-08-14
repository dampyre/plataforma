from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from plataforma.apps.workforce.forms import *
from plataforma.apps.workforce.models import *


def vista_hw(request):
	monitor = Monitor.objects.all()
	mouse = Mouse.objects.all()
	teclado = Teclado.objects.all()
	impresoras = Impresoras.objects.all()
	cxmobiles = Conexiones_moviles.objects.all()
	cpu = CPU.objects.all()
	note = NoteBook.objects.all()
	ctx = {'monitor': monitor, 'mouse':mouse, 'teclado': teclado, 'impresoras':impresoras, 'conexiones': cxmobiles, 'CPU':cpu, 'note': note}
	return render_to_response ('mantenedor/vista_hw.html', ctx, context_instance=RequestContext(request))

def nuevoMonitor(request):
	if request.method=='POST':
		formulario = formMonitor(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/mantenedor')
	else:
		formulario = formMonitor()

	return render_to_response("mantenedor/formMonitor.html", {'formulario': formulario}, context_instance=RequestContext(request))
		
			