from django.shortcuts import render, redirect
from django.core.mail import send_mail
from listings.models import Band, Listing
from listings.forms import ContactUsForm, BandForm, ListingForm

# interface crud des modeles
## band
### read all
def band_list(request):
    bands = Band.objects.all()
    return render(request, "listings/bands.html", {"bands" : bands})

### read one
def band_details(request, id):
    band = Band.objects.get(id=id)
    return render(request, "listings/band_details.html", {"band" : band})

### create
def band_create(request):
    if request.method == "POST":
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band_details', band.id)
    else:
        form = BandForm()
    return render(request, 'listings/band_create.html', {'form' : form})

### update
def band_update(request, id):
    band = Band.objects.get(id=id)
    if request.method == "POST":
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            form.save()
            return redirect('band_details', band.id)
    else:
        form = BandForm(instance=band)
    return render(request, 'listings/band_update.html', {'form' : form})

### delete
def band_delete(request, id):
    band = Band.objects.get(id=id)
    if request.method == "POST":
        band.delete()
        return redirect('bands')
    return render(request, 'listings/band_delete.html', {'band' : band})


## listing
### read all
def listings(request):
    listings = Listing.objects.all()
    return render(request, "listings/listings.html", {"listings" : listings})

### read one
def listing_details(request, id):
    listing = Listing.objects.get(id=id)
    return render(request, "listings/listing_details.html", {"listing" : listing})

### create
def listing_create(request):
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save()
            return redirect('listing_details', listing.id)
    else:
        form = ListingForm()
    return render(request, 'listings/listing_create.html', {'form' : form})

### update
def listing_update(request, id):
    listing = Listing.objects.get(id=id)
    if request.method == "POST":
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('listing_details', listing.id)
    else:
        form = ListingForm(instance=listing)
    return render(request, 'listings/listing_update.html', {'form' : form})

### delete
def listing_delete(request, id):
    listing = Listing.objects.get(id=id)
    if request.method == "POST":
        listing.delete()
        return redirect('listings')
    return render(request, 'listings/listing_delete.html', {'listing' : listing})


# vue about
def about_us(request):
    return render(request, "listings/about_us.html")

# vue confirmation d'envoi de mail
def email_sent(request):
    return render(request, 'listings/email_sent.html')

#vue contact
def contact_us(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f"Message from {form.cleaned_data['name']} or 'anonyme' via Merchex Contact Us form",
                message=form.cleaned_data["message"],
                from_email=form.cleaned_data["email"],
                recipient_list=["admin@merchex.xyz"]
            )
            return redirect('email_sent')
    else:
        form = ContactUsForm()
    return render(request, "listings/contact_us.html", {"form" : form})