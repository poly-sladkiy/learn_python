"""samplesite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


"""
    По мнению автора использование псевдонимов - порождает путаницу.
"""
app_name = 'bboard'
urlpatterns = [
    # Корневой маршрут, указывающий на "корень" самого веб-сайта
    path('', include(('bboard.urls', 'default-bboard'), namespace='default-bboard')),

    # Псевдоним - альтернативное имя
    # В html коде его можно указать как:
    # <a href="{% 'other-bboard:index' %}">...</a>
    path('bboard/', include(('bboard.urls', 'other-bboard'), namespace='other-bboard')),
    path('admin/', admin.site.urls),
]
