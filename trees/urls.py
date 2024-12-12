from django.urls import path
from . import views

urlpatterns = [
    path('plant/', views.PlantTreeView.as_view(), name='plant_tree'),
    path('', views.ViewPlantedTreesView.as_view(), name='view_planted_trees'),
    path('accounts/', views.ViewAccountTreesView.as_view(), name='view_account_trees'),
]
