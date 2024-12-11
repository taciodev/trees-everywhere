from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from accounts import views

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
]
