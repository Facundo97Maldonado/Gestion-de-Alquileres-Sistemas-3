from Inmobiliaria.models import *
from django.contrib import admin

class AdminCiudades(admin.ModelAdmin):
	search_fields = ['nombre']

class AdminPropiedad(admin.ModelAdmin):
	search_fields = ['codigo']
	list_filter = ('ciudad',)
	ordering = ('titulo',)

# Register your models here.
admin.site.register(FechaAlquiler)
admin.site.register(Ciudad, AdminCiudades)
admin.site.register(Reserva)
admin.site.register(Huesped)
admin.site.register(Propiedad)