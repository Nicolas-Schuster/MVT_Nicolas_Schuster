from django.shortcuts import render
from django.http import HttpResponse
from MVT_app_entregable.models import family


def new_member(request):
    family.objects.create(fist_name = 'Hector', last_name = 'Acencio', age  = 76, life = True, male = True)
    return HttpResponse('Nuevo miembro en la famillia')


def list_members(request):
    all_family_members = family.objects.all()
    context = {
        'family_members':all_family_members,
    }
    return render(request, 'list_members.html', context=context)
