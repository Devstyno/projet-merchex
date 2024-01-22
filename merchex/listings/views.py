from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listing

def hello(request):
    bands = Band.objects.all()
    return render(request, "listings/hello.html", {"bands" : bands})

def listings(request):
    listings = Listing.objects.all()
    return render(request, "listings/listings.html", {"listings" : listings})

def about_us(request):
    return render(request, "listings/about_us.html")

def contact_us(request):
    return render(request, "contact_us.html")