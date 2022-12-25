from django.http import HttpResponse
from django.shortcuts import render


def inicio(request):
    context = {
        'raiz':'Bienvenidos al INICIO',
        'intro':'Daremos un pequeño paseo por mi pequeña famillia y algunos amigos ',
        'sufri':'me costo bastante entender lo que habia que hacer jaja',
        'trunk':'Para ver a mi famillia ingrese a '  ' ¨famillia/¨ ',
        'branch':'Para ver a mis amigos ingrese a '  ' ¨amigos/¨ '
    }
    return render(request, 'inicio.html', context=context)