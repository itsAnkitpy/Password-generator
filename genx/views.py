from django.shortcuts import render
import random

def index(request):
    characters= list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('numbers'):
        characters.extend('0123456789')
    if request.GET.get('symbols'):
        characters.extend('!@#$%^&*()_+|":?><')

    length = request.GET.get('length', 12)

    thepassword = ""

    for x in range(int(length)):
        thepassword += random.choice(characters) 

    return render(request, 'genx/index.html', {'password': thepassword})


