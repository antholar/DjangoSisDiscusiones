from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView # Se importa la vista generica de django
# Create your views here.

class IndexView(TemplateView): #por herencia se jala todos los atributos de la clase generica de dj 
	template_name = 'home/index.html' # propiedad de la vista generica, se le asigno ese template
