from django.shortcuts import render
#from django.http import HttpResponse
import random

# Create your views here.
#Esta carpeta es para decir que funciones podemos ejecutar cuando visiten nuestra app

def explicacion(request):
    return render(request, 'generador/explicacion.html')   

def home(request):
    return render(request, 'generador/home.html')

#Este def es para que me cree numeros caracteres aleatorios, dentro del rango de length,que puede variar dependiendo su valor escogido
def password(request):
    
    charecters = list('abcdefghijklmnñopqrstuvwxyz')
    generated_password = ''

    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):    
        charecters.extend(list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        charecters.extend(list('!@#$%&*()'))

    if request.GET.get('numbers'):
        charecters.extend(list('1234567890'))

    for x in range(length):
        generated_password += random.choice(charecters)

    return render(request, 'generador/password.html', {'password': generated_password})