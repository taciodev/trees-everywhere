from django.urls import path
from . import views

urlpatterns = [
    path('plant/', views.plant_tree, name='plant_tree'),
    path('my_trees/', views.my_trees, name='my_trees'),
    path('account_trees/', views.account_trees, name='account_trees'),
]
