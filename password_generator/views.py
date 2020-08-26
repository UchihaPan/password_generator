from django.shortcuts import render
import random
from .choices import Choices


def home(request):
    context = {
        'Choices': Choices
    }
    return render(request, 'password_generator/home.html', context)


def password(request):
    character = list('abcdefghijklmnopqrstuvwxyz')
    if 'uppercase' in request.GET:
        character.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if 'special' in request.GET:
        character.extend(list('!@#$%^&{}/,.*()'))
    if 'numbers' in request.GET:
        character.extend(list('0123456789'))
    if 'length' in request.GET:
        length = int(request.GET['length'])


    password = ''
    for _ in range(length):
        password += random.choice(character)

    return render(request, 'password_generator/password.html', {'password': password})
