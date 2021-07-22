from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path

from .views import index, BbCreateView, BbByRubricView, BbDetailView, rubrics

# Имя приложения
app_name = 'bboard'
urlpatterns = [

    path('add/', BbCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', BbByRubricView.as_view(), name='by_rubric'),
    path('detail/<int:pk>/', BbDetailView.as_view(), name='detail'),
    path('rubrics/', rubrics, name='edit_rubrics'),

    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),

    path('accounts/password_change/', PasswordChangeView.as_view(
        template_name='registration/change_password.html'),
        name='change_password'),
    path('accounts/password_change/done', PasswordChangeDoneView.as_view(
        template_name='registration/password_changed.html'), name='password_change_done'),
    path('accounts/password_reset/', PasswordResetView.as_view(
        template_name='registration/reset_password.html',
        subject_template_name='registration/reset_subject.txt',
        email_template_name='registration/reset_email.txt'),
        name='password_reset'),
    path('accounts/password_reset/done/', PasswordResetDoneView.as_view(
        template_name='registration/email_sent.html'),
        name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>',
         PasswordResetConfirmView.as_view(
             template_name='registration/confirm_password.html'),
         name='password_reset_confirm'),
    path('accounts/reset/done/',
         PasswordResetCompleteView.as_view(
             template_name='registration/password_confirmed.html'),
         name='password_reset_complete'),

    # Корневой маршрут, указывающий на "корень" приложения bboard
    path('', index, name='index'),
]
