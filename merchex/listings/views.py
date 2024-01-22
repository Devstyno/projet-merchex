from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listing

def hello(request):
    bands = Band.objects.all()
    return render(request, "listings/hello.html", {"bands" : bands})

def about_us(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons Merch !</p>')

def listings(request):
    listings = Listing.objects.all()
    return HttpResponse(f"""
        <h1>Annonces</h1>
        <p>Bientot, nous aurons :<p>
        <ul>
            <li>{listings[0].title}</li>
            <li>{listings[1].title}</li>
            <li>{listings[2].title}</li>
            <li>{listings[3].title}</li>
        </ul>
""")

def contact_us(request):
    return HttpResponse('<h1>Contactez-nous</h1> <p>Formulaire bientot disponible</p>')