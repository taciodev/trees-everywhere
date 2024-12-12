from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Tree
from accounts.models import PlantedTree, User, Account, UserAccount
from .forms import PlantedTreeForm


@login_required
def plant_tree(request):
    """
    View to plant a tree.
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
    account_id = request.GET.get('account')

    if account_id:
        account = get_object_or_404(Account, id=account_id)
        account_trees = PlantedTree.objects.filter(
            user=request.user, 
            account=account, 
            account__in=UserAccount.objects.filter(user=request.user).values_list('account', flat=True)
        )
    else:
        account = None
        account_trees = []

    user_accounts = Account.objects.filter(
        id__in=UserAccount.objects.filter(user=request.user).values_list('account', flat=True)
    )
    context = {
        'user_accounts': user_accounts,
        'account': account,
        'account_trees': account_trees,
    }
    return render(request, 'trees/account_trees.html', context)
