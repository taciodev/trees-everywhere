from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import PlantedTree, User


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
    return render(request, 'trees/account_trees.html')
