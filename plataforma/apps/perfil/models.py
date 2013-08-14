from django.db import models
#importando libreria para generar los thumbsnail miniaturas de img
from thumbs import ImageWithThumbsField
from plataforma.apps.workforce.models import NoteBook,Equipo,Conexiones_moviles
import datetime

# Create your models here.


class Servicios(models.Model):

    nombre_servicio = models.CharField(max_length=50 )
    Direccion_servicio = models.CharField(max_length=100)
    usuario_servicio = models.CharField(max_length=50)
    password_servicio = models.CharField(max_length=50)
    fecha_ingreso = models.DateTimeField(default=datetime.datetime.now)
    status = models.BooleanField(default=True)

    def __unicode__(self):

        return self.nombre_servicio


class Perfil(models.Model):

    def url(self, filename):
        ruta = "MultimediaData/avatar/%s/%s" % (self.nick, str(filename))
        return ruta

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nick = models.CharField(max_length=30)
    correo = models.EmailField()
    clave_correo = models.CharField(max_length=20, blank= True)
    imagen = ImageWithThumbsField(upload_to=url, sizes=((125, 125), (200, 200)),
         null= True, blank= True)

    servicio = models.ManyToManyField(Servicios, blank = True)
    equipo = models.OneToOneField(Equipo)
    conexion = models.OneToOneField(Conexiones_moviles)
    notebook = models.OneToOneField(NoteBook,)


    def __unicode__(self):

        return self.nick




