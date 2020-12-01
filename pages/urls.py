from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listyourcar', views.listyourcar, name='listyourcar')
]
