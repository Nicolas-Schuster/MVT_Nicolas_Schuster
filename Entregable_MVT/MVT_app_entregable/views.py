from django.shortcuts import render
from django.http import HttpResponse
from MVT_app_entregable.models import family, friends


def new_member(request):
    family.objects.create(fist_name = 'Horacio', last_name = 'Schuster', age  = 74, life = True, male = True)
    return HttpResponse('Nuevo miembro en la famillia')


def list_members(request):
    all_family_members = family.objects.all()
    context = {
        'family_members':all_family_members,
    }
    return render(request, 'list_members.html', context=context)


def new_friend(request):
    friends.objects.create(name = 'Alejandro', age = 25, male = True)
    return HttpResponse('Haz hecho un nuevo amigo felicidades')


def list_friends(request):
    all_friends = friends.objects.all()
    context = {
        'friends': all_friends
    }
    return render(request, 'list_friends.html', context=context)