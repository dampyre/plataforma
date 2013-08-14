from django.conf.urls import * 

urlpatterns = patterns('plataforma.apps.workforce.views',
	url(r'^mantenedor/', 'vista_hw', name='vista_hw'),
	url(r'^formulario/$', 'nuevoMonitor', name='nuevoMonitor'),
 )