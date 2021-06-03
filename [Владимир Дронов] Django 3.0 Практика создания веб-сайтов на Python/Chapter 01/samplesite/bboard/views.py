from django.shortcuts import render

from .models import Bb


def index(requests):
    bbs = Bb.objects.all()
    return render(requests, 'bboard/index.html', {'bbs': bbs})
