from typing import List, Tuple
from decimal import Decimal

from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.models import (
    Account,
)
from trees.models import Tree
from trees.repositories import PlantedTreeRepository


class User(AbstractUser):
    """A custom user model that extends the AbstractUser model."""

    accounts = models.ManyToManyField(
        "accounts.Account", through="accounts.UserAccount", related_name="users"
    )

    def plant_tree(self, tree: Tree, location: Tuple[Decimal, Decimal], account):
        """Plants a single tree for the user."""
        if not isinstance(tree, Tree):
            raise ValidationError("Invalid tree instance.")
        if not isinstance(account, Account):
            raise ValidationError("Invalid account instance.")
        if not isinstance(location, tuple) or len(location) != 2:
            raise ValidationError(
                "Invalid location. Location must be a tuple of (latitude, longitude)."
            )

        try:
            return PlantedTreeRepository.create_planted_tree(
                self, tree, location, account
            )
        except Exception as e:
            raise ValidationError(f"Error planting tree: {e}")

    def plant_trees(self, plants: List[Tuple[Tree, Tuple[Decimal, Decimal], Account]]):
        """Plants multiple trees for the user."""
        return [
            self.plant_tree(tree, location, account)
            for tree, location, account in plants
        ]


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
