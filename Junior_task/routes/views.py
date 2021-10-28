from django.contrib import messages
from django.shortcuts import render

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
