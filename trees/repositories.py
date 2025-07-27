from .models import Tree, PlantedTree
from accounts.models import Account, UserAccount


class TreeRepository:
    """Repository for managing Tree objects."""

    def get_tree_names(self):
        """Retrieves a list of tree names."""
        return Tree.objects.values_list("name", flat=True)


class PlantedTreeRepository:
    @staticmethod
    def create_planted_tree(user, tree, location, account):
        """Creates a PlantedTree object and saves it to the database."""
        planted_tree = PlantedTree(
            user=user,
            tree=tree,
            account=account,
            latitude=location[0],
            longitude=location[1],
        )
        planted_tree.save()
        return planted_tree

    @staticmethod
    def get_trees_by_user(user):
        """Return trees planted by the user."""
        return PlantedTree.objects.filter(user=user)

    @staticmethod
    def get_trees_by_user_and_account(user, account):
        """Return trees planted by the user in a specific account."""

        return PlantedTree.objects.filter(
            user=user,
            account=account,
            account__in=UserAccount.objects.filter(user=user).values_list(
                "account", flat=True
            ),
        )

    def get_accounts_by_user(self, user):
        """Return accounts associated with the user."""
        return Account.objects.filter(
            id__in=UserAccount.objects.filter(user=user).values_list(
                "account", flat=True
            )
        )

    def save(self, planted_tree):
        """Saves a PlantedTree object to the database."""
        planted_tree.save()
