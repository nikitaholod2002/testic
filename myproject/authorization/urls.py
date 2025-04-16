from django.urls import path, include
from . import views



urlpatterns = [
    path('registration/', views.registration),
    path('', views.authorization),
]
