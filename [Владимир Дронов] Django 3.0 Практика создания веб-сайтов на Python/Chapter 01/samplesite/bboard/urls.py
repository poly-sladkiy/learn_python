from django.urls import path

from .views import index, by_rubric, BbCreateView, add_save, add

# Имя приложения
app_name = 'bboard'
urlpatterns = [
    path('add/save/', add_save, name='add_save'),
    path('add/', add, name='add'),

    path('add/', BbCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),

    # Корневой маршрут, указывающий на "корень" приложения bboard
    path('', index, name='index'),
]
