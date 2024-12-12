from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class CoreView(LoginRequiredMixin, TemplateView):
    """Render the core page."""
    template_name = 'core/index.html'
