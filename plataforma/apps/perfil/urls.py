from django.conf.urls import * 

urlpatterns = patterns('plataforma.apps.perfil.views',
	url(r'^perfil/', 'vista_perfil', name='vista_perfil'),
	url(r'^mantenedor/(?P<id_perfil>.*)/$', 'vista_completa', name='vista_completa'),

)