from django import forms
from plataforma.apps.perfil.models import Servicios 
from plataforma.apps.workforce.models import Equipo, Conexion, NoteBook

class FormPerfil (forms.Form):
	nombre = forms.CharField(widget=forms.TextInput())
	apellido = forms.CharField(widget=forms.TextInput())
	nick = forms.CharField(widget=forms.TextInput())
	correo = forms.EmailField(widget=validate_email)
	clave_correo = forms.CharField(widget=forms.TextInput())
	imagen = forms.ImageField(required=False)
	servicio = forms.ModelChoiseField(queryset=Servicios.objects.all())
	equipo = forms.ModelChoiseField(queryset = Equipo.objects.all())
	conexion = forms.ModelChoiseField(queryset = Conexion.objects.all())
	notebook = forms.ModelChoiseField(queryset = NoteBook.objects.all())

	
