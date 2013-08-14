from django.db import models

import datetime


# selescciones
tipo_impresora = (
    ('multi','Multifuncional-tinta'),
    ('multi-laser', 'Multifuncional-Laser'),
    ('laser', 'Laser'),
    ('laser-color', 'Laser Color'),
    ('ploter', 'Plotter'),
    ('matriz', 'Matriz de punto'),
    )
conexion_monitor = (
    ('dvi', 'DVI'),
    ('vga', 'VGA'),
    ('hdmi', 'HDMI'),
    )
conexionimp = (
    ('usb', 'USB'),
    ('lan', 'LAN'),
    ('wifi', 'WI-FI'),
    ('serial', 'Serial LPT'),
    )
estados = (
    ('uso', 'En uso'),
    ('mal', 'Mal estado'),
    ('rep', 'En reparacion'),
    )
conexion_mouse = (
    ('usb', 'USB'),
    ('ps2', 'PS2'),
    ('bl', 'Bluetooth'),
    )
#datos bam
# compania movil
compania = (
    ('ent', 'Entel'),
    ('mov', 'Movistar'),
    ('clr', 'claro'),
    ('vrm', 'Virgin Mobile'),
    ('nxt', 'Nextel'),
    )
contrato = (
    ('pln', 'Plan'),
    ('prp', 'Prepago'),
    )


class Monitor (models.Model):

    tipo_pantalla = models.CharField(max_length=30)
    tam_pantall = models.CharField(max_length=10)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    tipo_conexion = models.CharField(max_length=30, choices=compania)
    fecha_ingreso = models.DateTimeField(default=datetime.datetime.now)
    num_serie = models.CharField(max_length=70)
    estado = models.CharField(max_length=10, choices=estados, default='uso')
    #status=activo inactivo
    status = models.BooleanField(default=True)

    def __unicode__(self):
        marcamodelo = "%s %s" % (self.marca, self.modelo)
        return marcamodelo

class Mouse (models.Model):

    modelo = models.CharField(max_length=40)
    marca = models.CharField(max_length=40)
    serie = models.CharField(max_length=40) 
    tipo_conexion = models.CharField(max_length=20, choices=conexion_mouse)
    fecha_ingreso = models.DateTimeField(default=datetime.datetime.now) 
    status = models.BooleanField(default=True) 

    def __unicode__(self):
        return self.modelo

class Teclado(models.Model):
    
    modelo = models.CharField(max_length=40)
    marca = models.CharField(max_length=40)
    serie = models.CharField(max_length=40)
    tipo_conexion = models.CharField(max_length=20, choices=conexion_mouse)
    estatus = models.BooleanField(default=True) 
    def __unicode__(self):
        marcamodelo = "%s %s" % (self.marca, self.modelo)
        return marcamodelo
        
class Impresoras(models.Model):

    modelo = models.CharField(max_length=40)
    marca = models.CharField(max_length=40)
    serie = models.CharField(max_length=40)
    tipo = models.CharField(max_length=40, choices=tipo_impresora)
    modelos_tinta = models.TextField()
    tipo_conexion = models.CharField(max_length=40, choices= conexionimp)
    IP = models.IPAddressField()
    fecha_ingreso = models.DateTimeField(default=datetime.datetime.now)
    estado = models.CharField(max_length=10, choices=estados, default='uso')
    estatus = models.BooleanField(default=True)

    def __unicode__(self):
        marcamodelo = "%s %s" % (self.marca, self.modelo)
        return marcamodelo

class Conexiones_moviles(models.Model):

    imei = models.CharField(max_length=40)
    numero = models.CharField(max_length=40)
    numero_sim = models.CharField(max_length=40)
    compania_movil = models.CharField(max_length=40, choices=compania, blank=True )
    tipo_contrato = models.CharField(max_length=10, choices=contrato, default='plan')
    marca_dispositivo = models.CharField(max_length=40)
    

    def __unicode__(self):
        num_compania = "%s %s" % (self.numero, self.compania_movil)
        return num_compania

class CPU(models.Model):

    marca = models.CharField(max_length= 40)
    modelo = models.CharField(max_length= 40)
    serie = models.CharField(max_length= 60)
    hdd = models.CharField(max_length= 10)
    ram = models.CharField(max_length= 10)
    fecha_ingreso = models.DateTimeField(default=datetime.datetime.now)
    estado = models.CharField(max_length=10, choices=estados, default='uso')
    estatus = models.BooleanField(default=True)

    def __unicode__(self):
        marcamodelo = "%s %s" % (self.marca, self.modelo)
        return marcamodelo


class Equipo (models.Model):

    direccion_ip = models.IPAddressField()
    nombre_equipo = models.CharField(max_length=50)
    fecha_activacion = models.DateTimeField(default=datetime.datetime.now)
    monitor = models.OneToOneField(Monitor)
    teclado = models.OneToOneField(Teclado)
    mouse = models.OneToOneField(Mouse)
    impresoras = models.ManyToManyField(Impresoras)
    cpu = models.OneToOneField(CPU)
    estatus = models.BooleanField(default=True)
    estado = models.CharField(max_length=10, choices=estados, default='uso')

class NoteBook(models.Model):

    marca = models.CharField(max_length= 50)
    modelo = models.CharField(max_length= 50)
    fecha_compra = models.DateTimeField(default=datetime.datetime.now)
    fecha_asignacion = models.DateTimeField(default=datetime.datetime.now)
    ram = models.CharField(max_length=10)
    hdd = models.CharField(max_length=10)
    estatus = models.BooleanField(default=True)
    estado = models.CharField(max_length=10, choices=estados, default='uso')
    
    def __unicode__(self):
        marcamodelo = "%s %s" % (self.marca, self.modelo)
        return marcamodelo




