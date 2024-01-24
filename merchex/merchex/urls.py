"""
URL configuration for merchex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from listings import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bands/', views.band_list, name='bands'),
    path('bands/<int:id>/', views.band_details, name='band_details'),
    path('bands/create/', views.band_create,name='band_create'),
    path('bands/<int:id>/update/', views.band_update,name='band_update'),
    path('listings/', views.listings, name='listings'),
    path('listings/<int:id>/', views.listing_details, name='listing_details'),
    path('listings/create/', views.listing_create,name='listing_create'),
    path('listings/<int:id>/update/', views.listing_update,name='listing_update'),
    path('about-us/', views.about_us, name='about'),
    path('contact-us/', views.contact_us, name='contact'),
    path('email_sent/', views.email_sent, name='email_sent')
]
