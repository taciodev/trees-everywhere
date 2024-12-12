from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, ListView

from accounts.models import Account, PlantedTree
from .repositories import PlantedTreeRepository, TreeRepository
from .forms import PlantedTreeForm


class PlantTreeView(LoginRequiredMixin, CreateView):
    """
    View to handle planting a new tree.
    """
    model = PlantedTree
    form_class = PlantedTreeForm
    template_name = 'trees/plant_tree.html'
    success_url = '/trees'
    repository = PlantedTreeRepository() 

    def get_initial(self):
        """
        Set initial values for the form.
        """
        initial = super().get_initial()
        initial['user'] = self.request.user.id
        return initial

    def form_valid(self, form):
        """
        Set the user before saving the form.
        """
        form.instance.user = self.request.user
        self.repository.save(form.instance)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """
        Add tree types to the context.
        """
        context = super().get_context_data(**kwargs)
        context['tree_types'] = TreeRepository().get_tree_names()  
        return context


class ViewPlantedTreesView(LoginRequiredMixin, ListView):
    """
    View to display the trees planted by the logged-in user.
    """
    model = PlantedTree
    template_name = 'trees/planted_trees.html'
    context_object_name = 'my_trees'
    repository = PlantedTreeRepository()  # Repository as attribute

    def get_queryset(self):
        """
        Return the trees planted by the logged-in user.
        """
        return self.repository.get_trees_by_user(self.request.user)


class ViewAccountTreesView(LoginRequiredMixin, ListView):
    """
    View to display trees planted within a specific account.
    """
    model = PlantedTree
    template_name = 'trees/account_trees.html'
    context_object_name = 'account_trees'
    repository = PlantedTreeRepository()  # Repository as attribute

    def get_queryset(self):
        """
        Return the trees planted by the user within the selected account.
        """
        account_id = self.request.GET.get('account')
        if account_id:
            account = get_object_or_404(Account, id=account_id)
            return self.repository.get_trees_by_user_and_account(self.request.user, account)
        else:
            return PlantedTree.objects.none()

    def get_context_data(self, **kwargs):
        """
        Add user accounts and selected account to the context.
        """
        context = super().get_context_data(**kwargs)
        context['user_accounts'] = self.repository.get_accounts_by_user(self.request.user)
        context['account_id'] = self.request.GET.get('account')
        return context