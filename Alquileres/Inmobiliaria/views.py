import datetime
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from Inmobiliaria.models import *
# Create your views here.

def index(request):
	props = Propiedad.objects.filter(fecha_alquileres__gt=datetime.datetime.now().date())
	return render_to_response('propiedad/index.html', {'propiedades' : props})

