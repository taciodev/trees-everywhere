from django.shortcuts import render
from django.contrib.auth.decorators import login_required


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
    return render(request, 'trees/planted_trees.html')


@login_required
def view_account_trees(request):
    """
    View to show the user's account trees.
    """
    return render(request, 'trees/account_trees.html')
