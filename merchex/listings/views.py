from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("<h1>Hello Django!</h1>")

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons Merch !</p>')

def listings(request):
    return HttpResponse('<h1>Annonces</h1> <p>Restez a l\'ecoute</p>')

def contact_us(request):
    return HttpResponse('<h1>Contactez-nous</h1> <p>Formulaire bientot disponible</p>')