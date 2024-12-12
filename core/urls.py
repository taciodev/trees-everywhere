from django.urls import path 
from core import views

urlpatterns = [
    path('', views.CoreView.as_view(), name='home'),
]