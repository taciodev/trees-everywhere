from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import PlantedTree, User, Account


@login_required
def plant_tree(request):
    """
    View to plant a tree.
    """
    return render(request, 'trees/plant_tree.html')


@login_required
def view_planted_trees(request):
    """
    View to show the planted trees.
    """
    user = User.objects.get(username=request.user)
    my_trees = PlantedTree.objects.filter(user=user)
    context = {'my_trees': my_trees}
    return render(request, 'trees/planted_trees.html', context)


@login_required
def view_account_trees(request):
    """
    View to show the user's account trees.
    """
    account_id = request.GET.get('account')  # Obtém o ID da conta do formulário

    if account_id:
        account = get_object_or_404(Account, id=account_id)
        account_trees = PlantedTree.objects.filter(user=request.user, account=account)
    else:
        account = None
        account_trees = []

    context = {
        'user_accounts': request.user.accounts.all(),  # Contas do usuário
        'account': account,
        'account_trees': account_trees,
    }
    return render(request, 'trees/account_trees.html', context)
