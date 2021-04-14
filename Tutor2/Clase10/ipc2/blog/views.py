from django.shortcuts import render
from django.template import Template, Context

posts = [
    {
        'autor':'Javier Lima',
        'titulo':'Laboratorio IPC2',
        'contenido':'Dando clase sobre el framework django',
        'fecha_post':'14 de abril de 2021'
    },
    {
        'autor':'Dennis Eduardo',
        'titulo':'Creando un proyecto',
        'contenido':'descripcion 1',
        'fecha_post':'15 de abril de 2021'
    },
    {
        'autor':'Luis Fernando Falla',
        'titulo':'Creando una aplicacion',
        'contenido':'descripcion 2',
        'fecha_post':'15 de abril de 2021'
    },
    {
        'autor':'Steven Gonzalez',
        'titulo':'Messiento con suenio',
        'contenido':'Steven se durmio tarde y esta cansado',
        'fecha_post':'14 de abril de 2021'
    }
]

# Create your views here.
def home(request):
    usuario = 'admin'
    contexto = {
        'posts':posts,
        'user':usuario
    }
    return render(request, 'home.html', contexto)

def about(request):
   return render(request, 'about.html', {'title':'About'})
