from django.conf.urls.defaults import patterns, url 

urlpatterns = patterns('plataforma.apps.home.views',
    url(r'^$', 'login_view', name='vista_login'),
    url(r'^index/', 'index_view', name='vista_principal'),
    url(r'^logout/$', 'logout_view', name='vista_logout'),

)