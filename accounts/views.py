from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def profile(request):
    #TODO: Add user profile data
    return render(request, 'registration/profile.html')
