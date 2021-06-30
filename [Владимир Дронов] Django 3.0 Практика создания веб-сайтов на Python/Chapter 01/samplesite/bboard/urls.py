from django.urls import path, re_path

from .views import index, by_rubric, BbCreateView

urlpatterns = [
    # Использование re для совместимости с django 1.x
    re_path(r'^add/$', BbCreateView.as_view(), name='add'),
    re_path(r'^(?P<rubric_id>[0-9]*)/$', by_rubric, name='by_rubric'),
    re_path(r'^$', index, name='index'),

    # path('add/', BbCreateView.as_view(), name='add'),
    # path('<int:rubric_id>/', by_rubric, name='by_rubric'),

    # Корневой маршрут, указывающий на "корень" приложения bboard
    # path('', index, name='index'),
]
