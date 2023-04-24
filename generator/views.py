from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    context = {
        'name': 'HVE',
        'bio': 'This is a short bio about me.'
    }
    return render(request, 'generator/about.html', context=context)

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    numbers = list('123456789')
    if request.GET.get('numbers'):
        characters.extend(list('123456789'))
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_-+={}[]:;|<>,.?/~`'))
    length = int(request.GET.get('length'))

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})