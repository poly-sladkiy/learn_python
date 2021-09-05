from django.shortcuts import render


def home(request):
    context = {'name': 'Django'}
    return render(request, 'home.html', context=context)
