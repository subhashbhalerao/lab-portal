from django.urls import path
from . import views

urlpatterns = [
    path('', views.labexam_home, name='labexam-home'),
]
