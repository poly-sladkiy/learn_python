from django.urls import path

from .views import index, by_rubric, BbCreateView, BbByRubricView, BbDetailView

# Имя приложения
app_name = 'bboard'
urlpatterns = [

    path('add/', BbCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', BbByRubricView.as_view(), name='by_rubric'),
    path('detail/<int:pk>/', BbDetailView.as_view(), name='detail'),

    # Корневой маршрут, указывающий на "корень" приложения bboard
    path('', index, name='index'),
]
