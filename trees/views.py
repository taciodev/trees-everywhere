from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import PlantedTree
from accounts.models import UserAccount, Account


@login_required
def plant_tree(request):
    """
    Render the tree planting page.
    """
    #TODO: Implementar a lógica para plantar uma árvore
    return render(request, 'trees/plant_tree.html')


@login_required
def my_trees(request):
    """
    Display the trees planted by the logged-in user.
    """
    user_accounts = UserAccount.objects.filter(user=request.user)
    planted_trees = PlantedTree.objects.filter(user__in=user_accounts)

    return render(request, 'trees/tree_list.html', {
        'planted_trees': planted_trees
    })


@login_required
def account_trees(request):
    """
    Display trees planted under the selected account for the logged-in user.
    """
    user_accounts = UserAccount.objects.filter(user=request.user) 
    accounts = [user_account.account for user_account in user_accounts]

    planted_trees = None
    selected_account = None

    if request.method == 'POST':
        selected_account_id = request.POST.get('account')
        selected_account = Account.objects.get(id=selected_account_id)
        planted_trees = PlantedTree.objects.filter(account=selected_account)

    return render(request, 'trees/account_tree_list.html', {
        'accounts': accounts,
        'planted_trees': planted_trees,
        'selected_account': selected_account
    })
