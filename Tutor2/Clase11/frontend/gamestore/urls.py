from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='gamestore-login'),
    path('login/', views.signin, name='signin'),
    path('home/', views.home, name='gamestore-home'),
    path('about/', views.about, name='gamestore-about'),
    path('registro/', views.registro, name='gamestore-registro'),
    path('signup/',views.signup, name='signup'),
]