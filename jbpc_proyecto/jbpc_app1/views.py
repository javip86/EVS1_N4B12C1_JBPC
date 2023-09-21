from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def display(request):
    return HttpResponse("<h1>Bienvenido a la página</h1> <br> <body> Contenido de la página </body> <h2> Subtítulo </h2> <p> Párrafo </p>")

def displayb(request):
    return HttpResponse("<p>Holaa</p> <br> <span> Esta es otra vista<span> <ol> Item 1 </ol> <ol> Item 2 </ol> <ol> Item 3</ol> <ol> Item 4</ol> <footer> Pie de página </footer>")

