from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Tree
from accounts.models import PlantedTree, User, Account
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
        form.fields['account'].queryset = Account.objects.filter(users=request.user)
    
    tree_types = Tree.objects.values_list('name', flat=True)
    user_accounts = request.user.accounts.all()

    context = {
        'form': form,
        'tree_types': tree_types,
        'user_accounts': user_accounts,
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
        account_trees = PlantedTree.objects.filter(user=request.user, account=account)
    else:
        account = None
        account_trees = []

    context = {
        'user_accounts': request.user.accounts.all(),
        'account': account,
        'account_trees': account_trees,
    }
    return render(request, 'trees/account_trees.html', context)
