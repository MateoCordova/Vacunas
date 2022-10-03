from django.urls import path

from . import views

app_name = 'vacunas'
urlpatterns = [
    # ex: /polls/5/
    path('', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('edit', views.edit, name='editar'),
    path('save', views.save, name='save')
]