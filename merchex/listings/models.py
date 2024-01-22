from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Band(models.Model):

    class Genre(models.TextChoices):
        HIP_HOP = "HH"
        SYNTH_POP = "SP"
        ALTERNATIVE_ROCK = "AR"
        RAP_FRANCAIS = "RF"
        GOSPEL = "G"

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices = Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2024)])
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)

class Listing(models.Model):

    class TypeAnnonce(models.TextChoices):
        DISQUES = "Records"
        VETEMENTS = "Clothing"
        AFFICHES = "Posters"
        AUTRES = "Miscellaneous"

    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2024)])
    type_annonce = models.fields.CharField(choices = TypeAnnonce.choices, max_length=20)