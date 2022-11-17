from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *
# Create your views here.

def index(request):
    return render(request, 'index.html')

def contacto_consulta(request):
    if request.method == "POST":
        formulario = CrearContacto(request.POST)

        if formulario.is_valid():

            formulario_contacto = formulario.cleaned_data

            contacto = Contacto(nombre=formulario_contacto["name"], email=formulario_contacto["email"], mensaje=formulario_contacto["message"])

            contacto.save()

            return render(request, "CinemaRevs/templates/index.html")
    else:
        formulario = CrearContacto()
        
    return render(request, "crearcontacto.html", {"formulario": formulario})

def catalog(request):

    films = Films.objects.all()

    context = {'films': films}

    return render(request, 'catalog.html', context=context)

def search_film(request):
     if request.GET.get('titulo', False):
        titulo = request.GET['titulo']

        found = Films.objects.filter(titulo__icontains=titulo)

        return render(request, "search_film.html", {"found":found})
     else:
        respuesta = "No results found"
    
     return render(request, 'search_film.html', {'respuesta': respuesta})

def add_film(request):

    if request.method == 'POST':

        addfilm = Add_Film(request.POST)

        if addfilm.is_valid():

            formulario_limpio = addfilm.cleaned_data

            newfilm = Films(titulo=formulario_limpio['titulo'], año=formulario_limpio['año'], genero=formulario_limpio['genero'], duracion=formulario_limpio['duracion'], sinopsis=formulario_limpio['sinopsis'])

            newfilm.save()

            return render(request, 'addfilm.html')

    else:
        addfilm = Add_Film()
    return render(request, 'addfilm.html', {'addfilm': Add_Film})


