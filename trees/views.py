from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from accounts.models import UserAccount, Account
from .models import Tree
from .repositories import PlantedTreeRepository
from .forms import PlantedTreeForm

@login_required
def plant_tree(request):
    """
    View to handle planting a new tree.
    """
    if request.method == 'POST':
        form = PlantedTreeForm(request.POST)
        if form.is_valid():
            tree = form.save(commit=False)
            tree.user = request.user
            tree.save()
            return redirect('view_planted_trees')
    else:
        form = PlantedTreeForm(initial={'user': request.user})
        user_accounts = UserAccount.objects.filter(user=request.user).values_list('account_id', flat=True)
        form.fields['account'].queryset = Account.objects.filter(id__in=user_accounts)

    tree_types = Tree.objects.values_list('name', flat=True)
    context = {
        'form': form,
        'tree_types': tree_types,
    }
    return render(request, 'trees/plant_tree.html', context)


@login_required
def view_planted_trees(request):
    """
    View to display the trees planted by the logged-in user.
    """
    repository = PlantedTreeRepository()
    my_trees = repository.get_trees_by_user(request.user)
    context = {'my_trees': my_trees}
    return render(request, 'trees/planted_trees.html', context)


@login_required
def view_account_trees(request):
    """
    View to display trees planted within a specific account.
    """
    repository = PlantedTreeRepository()
    
    account_id = request.GET.get('account')
    if account_id:
        account = get_object_or_404(Account, id=account_id)
        account_trees = repository.get_trees_by_user_and_account(request.user, account)
    else:
        account = None
        account_trees = []

    user_accounts = repository.get_accounts_by_user(request.user)
    context = {
        'user_accounts': user_accounts,
        'account': account,
        'account_trees': account_trees,
    }
    return render(request, 'trees/account_trees.html', context)