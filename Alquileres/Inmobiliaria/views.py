import datetime
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from Inmobiliaria.models import *
# Create your views here.

def indexView(request):
	props = Propiedad.objects.all()
	return render_to_response('Inmobiliaria/index.html', {'propiedades' : props})

