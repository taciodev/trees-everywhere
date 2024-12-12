from accounts.models import UserAccount, Account, PlantedTree
from .models import Tree


class TreeRepository:
    """
    Repository for managing Tree objects.
    """

    def get_tree_names(self):
        """
        Retrieves a list of tree names.
        """
        return Tree.objects.values_list('name', flat=True)


class PlantedTreeRepository:

    def get_trees_by_user(self, user):
        """
        Return trees planted by the user.
        """
        return PlantedTree.objects.filter(user=user)

    def get_trees_by_user_and_account(self, user, account):
        """
        Return trees planted by the user in a specific account.
        """
        return PlantedTree.objects.filter(
            user=user, 
            account=account, 
            account__in=UserAccount.objects.filter(user=user).values_list('account', flat=True)
        )

    def get_accounts_by_user(self, user):
        """
        Return accounts associated with the user.
        """
        return Account.objects.filter(
            id__in=UserAccount.objects.filter(user=user).values_list('account', flat=True)
        )
    
    def save(self, planted_tree):
        """
        Saves a PlantedTree object to the database.
        """
        planted_tree.save()