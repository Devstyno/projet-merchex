from django.shortcuts import render
from listings.models import Band, Listing

def band_list(request):
    bands = Band.objects.all()
    return render(request, "listings/band_list.html", {"bands" : bands})

def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request, "listings/band_detail.html", {"band" : band})

def listings(request):
    listings = Listing.objects.all()
    return render(request, "listings/listings.html", {"listings" : listings})

def about_us(request):
    return render(request, "listings/about_us.html")

def contact_us(request):
    return render(request, "listings/contact_us.html")