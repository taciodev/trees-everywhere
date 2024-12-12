from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class RegisterView(TemplateView):
    """Register a new user."""
    template_name = 'accounts/register.html'


class ProfileView(LoginRequiredMixin, TemplateView):
    """Display the user's profile."""
    template_name = 'accounts/profile.html'