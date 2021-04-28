from django.shortcuts import render
from .forms import LoginForm, RegisterForm
import requests
# Create your views here.
endpoint = 'http://127.0.0.1:5000/'
def home(request):
    response = requests.get(endpoint+'games');
    games = response.json()
    contexto = {
        'games' : games
    }
    return render(request, 'store.html', contexto)

def about(request):
    return None

def login(request):
    context = {
        'title':'Login'
    }
    return render(request, 'login.html', context)

def registro(request):
    context = {
        'title':'Registro'
    }
    return render(request, 'signup.html', context)

def signin(request):
    contexto ={}
    if request.method == 'GET':
        form = LoginForm(request.GET)
        if form.is_valid():
            user = form.cleaned_data['username']
            passw  =form.cleaned_data['password']
            r = requests.get(endpoint+'/login/'+user+'/'+passw);
            data = r.json()
            print(data['data'])
            if data['data']==True:
                response = requests.get(endpoint+'games');
                games = response.json()
                contexto = {
                'games' : games,
                'user':user
                }
    return render(request, 'store.html', contexto)

def signup(request):
    contexto ={}
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        #print(form)
        if form.is_valid():
            name = form.cleaned_data['name']
            lastname = form.cleaned_data['lastname']
            user = form.cleaned_data['username']
            passw  =form.cleaned_data['password']
            pload = {'nombre':name,'apellido':lastname,'usuario':user,'password':passw}
            r = requests.post(endpoint+'/registro', json=pload);
            print(r.status_code)
        else:
            print('F')
    return render(request, 'login.html', contexto)

