from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Reserva de una propiedad
class Reserva(models.Model):
	numero_reserva = models.IntegerField()
	fecha_reserv = models.DateTimeField()
	total = models.DecimalField(max_digits = 6, decimal_places = 2)

	def get_fechaAlquiler(self):
		return self.fechaAlquileres_set.all()

# Fecha de alquiler de la propiedad
class FechaAlquiler(models.Model):
	fecha_reserva = models.ForeignKey(Reserva)

	class Meta:
		verbose_name_plural = 'fechaAlquileres'

# Ciudades que contienen propiedades
class Ciudad(models.Model):
	nombre = models.CharField(max_length = 50)

	class Meta:
		verbose_name_plural = 'Ciudades'

	def __str__ (self):
		return self.nombre

	def get_propiedades(self):
		return self.propiedades_set.all()

# Huesped de una propiedad
class Huesped(models.Model): #tiene 1 reserva
	nombre = models.CharField(max_length = 50)
	apellido = models.CharField(max_length = 50) 
	email = models.EmailField()

	def __str__ (self):
		return self.nombre + ', ' + self.apellido;

	class Meta:
		verbose_name_plural = 'Huespedes'

# Propiedad en si
class Propiedad (models.Model):

	descripcion = models.CharField(max_length=50)
	precio_diario = models.DecimalField(max_digits = 6, decimal_places = 2)
	imagen = models.CharField(null = True, blank = True, max_length = 200)
	titulo = models.CharField(max_length=50)
	numero_ficha = models.IntegerField()
	max_pax = models.IntegerField()
	fecha_alquileres = models.ManyToManyField(FechaAlquiler) #isDisponible
	ciudad = models.ForeignKey(Ciudad)
	reserva = models.ForeignKey(Reserva)
	anfitrion = models.ForeignKey(User)
	
	def __str__ (self):
		return self.descripcion;
	
	class Meta:
		verbose_name_plural = 'Propiedades'

