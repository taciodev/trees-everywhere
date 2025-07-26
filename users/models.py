from decimal import Decimal
from typing import Tuple

from django.db import models
from django.contrib.auth.models import AbstractUser
from trees.models import Tree


class User(AbstractUser):
    """A custom user model that extends the AbstractUser model."""

    accounts = models.ManyToManyField(
        "accounts.Account", through="accounts.UserAccount", related_name="users"
    )

    def plant_tree(self, tree: Tree, location: Tuple[Decimal, Decimal], account):
        from trees.repositories import PlantedTreeRepository

        return PlantedTreeRepository.create_planted_tree(self, tree, location, account)

    def plant_trees(self, plants):
        list_of_planted_trees = []
        for tree, location, account in plants:
            planted = self.plant_tree(tree, location, account)
            list_of_planted_trees.append(planted)
        return list_of_planted_trees


class Profile(models.Model):
    """A model to represent a user profile."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField(blank=True)
    joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfis"

    def __str__(self):
        return self.user.username
