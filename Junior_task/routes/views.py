from django.contrib import messages
from django.shortcuts import render, redirect

from routes.forms import RouteForm
from routes.utils import get_route


def home(request):
    form = RouteForm()
    return render(request, 'routes/home.html', {'form': form})


def find_routes(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)

        if form.is_valid():
            try:
                context = get_route(request, form)

            except ValueError as er:
                messages.error(request, er)
                return render(request, 'routes/home.html', {'form': form})

            return render(request, 'routes/home.html', context=context)

        return render(request, 'routes/home.html', {'form': form})

    else:
        form = RouteForm()
        messages.error(request, "Нет данных для поиска")
        return render(request, 'routes/home.html', {'form': form})


def add_route(request):
    if request.method == 'POST':
        context = {}
        data = request.POST
        return render(request, 'routes/create.html', context)

    else:
        messages.error(request, "Не возможно сохранить несуществующий маршрут")
        return redirect('/')
