from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('random_string', views.random),
    path('reset', views.reset),
]
