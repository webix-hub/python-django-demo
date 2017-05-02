from django.db import models
from django.core import serializers
from django.forms import ModelForm

class Film(models.Model):
	title	= models.CharField(max_length=200)
	year	= models.IntegerField()
	votes	= models.IntegerField()
	rating	= models.FloatField()
	rank	= models.IntegerField()

class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = [
            'title', 'year', 'votes', 'rating', 'rank'
        ]
