from django.shortcuts import render

from .models import Bb


def index(requests):
    bbs = Bb.objects.order_by('-published')
    return render(requests, 'bboard/index.html', {'bbs': bbs})
