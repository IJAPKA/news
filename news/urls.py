from django.urls import path
from . import views  # Импортируем views

urlpatterns = [
    path('example/', views.example_view, name='example_view'),
]