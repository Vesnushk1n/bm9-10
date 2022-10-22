from django.urls import path, include
from . import views

urlpatterns = [
    path('start', views.start, name='start'),
    path('end', views.end, name='end'),
]