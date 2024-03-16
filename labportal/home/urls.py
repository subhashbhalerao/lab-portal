from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=''),
    path('lab-rules/', views.lab_rules, name='lab-rules'),
]