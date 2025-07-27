from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class RegisterView(TemplateView):
    """Register a new user."""

    template_name = "users/register.html"


class ProfileView(LoginRequiredMixin, TemplateView):
    """Display the user's profile."""

    template_name = "users/profile.html"
