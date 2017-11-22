from django.conf.urls import include, url
from django.contrib import admin
from Inmobiliaria.views import *

urlpatterns = [
    url(r'^$', index),
    url(r'hosts/', hosts),
    url(r'estate/(?P<id_estate>\d+)/reserve', index_reserve, name="estate_reserve")
]
