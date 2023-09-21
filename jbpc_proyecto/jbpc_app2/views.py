from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def displayvist(request):
    return HttpResponse("<head> Cabeza de página </head> <h2>Vista app 2 </h2> <ul>Item 1 </ul> <ul>Item 2 </ul><ul>Item 3 </ul> <p> Párrafo </p>")

def displayDateTime(request):
    now = datetime.datetime.now()
    return HttpResponse (now)

def displaydatos(request):
    return HttpResponse("<h3>Esta es una vista</h3> <br> <p>Párrafo normal</p> <span>Párrafo resaltado</span> <footer> Pie de página</footer>")