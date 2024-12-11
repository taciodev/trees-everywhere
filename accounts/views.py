from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def register(request):
    """
    Register a new user
    """
    return render(request, 'accounts/register.html')

@login_required
def profile(request):
    """
    Display the user's profile
    """
    return render(request, 'accounts/profile.html')
