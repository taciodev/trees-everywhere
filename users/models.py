from decimal import Decimal
from typing import Tuple, List

from django.db import models
from django.contrib.auth.models import AbstractUser
from trees.models import Tree


class User(AbstractUser):
    """A custom user model that extends the AbstractUser model."""

    accounts = models.ManyToManyField(
        "accounts.Account", through="accounts.UserAccount", related_name="users"
    )

    def plant_tree(self, tree: Tree, location: Tuple[Decimal, Decimal]):
        from trees.repositories import PlantedTreeRepository

        PlantedTreeRepository.create_planted_tree(self, tree, location)

    def plant_trees(self, plants: List[Tuple[Tree, Tuple[Decimal, Decimal]]]):
        for tree, location in plants:
            self.plant_tree(tree, location)


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
