from django import forms
from django.utils.timezone import now

class CrearReview(forms.Form):
    nombre = forms.CharField(max_length=40)
    texto = forms.CharField(max_length=250)
    fecha = forms.DateField()

class CrearContacto(forms.Form):
    name = forms.CharField(max_length=40)
    email = forms.EmailField(max_length=90)
    message = forms.CharField(max_length=250)

class Add_Film(forms.Form):
    titulo = forms.CharField(max_length=40)
    año = forms.IntegerField()
    duracion = forms.IntegerField()
    genero = forms.CharField(max_length=40)
    sinopsis = forms.CharField(max_length=250)
