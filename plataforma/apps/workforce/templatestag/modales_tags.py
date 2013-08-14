from django import template
from plataforma.apps.workforce.models import *



register = template.Library()
@register.inclusion_tag('/mantenedor/formMonitor.html', takes_context=True)

def formMonitor(context):
	if request.method=='POST':
		formulario = formMonitor(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/mantenedor')
	else:
		formulario = formMonitor()
	return {'formulario':formulario}
