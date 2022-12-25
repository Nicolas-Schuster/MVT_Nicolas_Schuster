from django.http import HttpResponse
from django.shortcuts import render


def inicio(request):
    context = {
        'raiz':'Bienvenidos al INICIO',
        'intro':'Daremos un pequeño paseo por mi pequeña famillia ',
        'sufri':'me costo bastante entender lo que habia que hacer jaja',
    }
    return render(request, 'inicio.html', context=context)