import json

from django.http import request
from django.shortcuts import render, redirect

# Create your views here.
# ---------------------Views---------------------------
from django.views.generic import TemplateView
from pip._vendor import requests


class HomeTemplateView(TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HomeTemplateView, self).get_context_data(*args, **kwargs)
        response = requests.get('http://weatherapicore.azurewebsites.net/api/cities?PageNumber=1&PageSize=15')

        citiesData = response.json()
        print(citiesData)
        context['cities'] = citiesData
        context['titulo'] = "Inicio"
        context['inicio_activo'] = 'active'
        return context


# Get cities with parametres
# def getCities(PageNumber,PageSize):
#     response = requests.get('http://freegeoip.net/json/')
#     geodata = response.json()


def postCities(request):
    response = requests.post('http://weatherapicore.azurewebsites.net/api/cities?PageNumber=1&PageSize=15')
    citiesData = response.json()
    return redirect('home')






