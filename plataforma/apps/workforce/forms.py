from django import forms
from django.forms import ModelForm
from plataforma.apps.workforce.models import * 




class formMonitor(ModelForm):
	class Meta:
		model = Monitor
		
class formMouse(ModelForm):
	class Meta:
		model = Mouse

class formTeclado(ModelForm):
	class Meta:
		model = Teclado

class formImpresoras(ModelForm):
	class Meta:
		model = Impresoras

class formConexiones_moviles(ModelForm):
	class Meta:
		model = Conexiones_moviles

class formCPU(ModelForm):
	class Meta:
		model = CPU

class formEquipo(ModelForm):
	class Meta:
		model = Equipo

class formNoteBook(ModelForm):
	class Meta:
		model = NoteBook

