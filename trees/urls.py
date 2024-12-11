from django.urls import path
from . import views

urlpatterns = [
    path('plant/', views.plant_tree, name='plant_tree'),
    path('', views.view_planted_trees, name='view_planted_trees'),
    path('accounts/', views.view_account_trees, name='view_account_trees'),
]
