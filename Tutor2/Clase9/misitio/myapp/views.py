from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hola que tal, soy el chico de las poesias xdxd </h1>")

def despedida(request):
    return HttpResponse("<h3> Adios :V </h3>")