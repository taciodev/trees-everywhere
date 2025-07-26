from decimal import Decimal
from django.db import models
from django.contrib.auth.models import AbstractUser
from trees.models import Tree

from trees.repositories import PlantedTreeRepository


class Account(models.Model):
    """A model to represent an account in the system."""

    name = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Conta"
        verbose_name_plural = "Contas"

    def __str__(self):
        return self.name


class User(AbstractUser):
    """A custom user model that extends the AbstractUser model."""

    accounts = models.ManyToManyField(
        Account, through="UserAccount", related_name="users"
    )

    def plant_tree(self, tree: Tree, location: tuple[Decimal, Decimal]):
        """Plant a tree."""
        PlantedTreeRepository.create_planted_tree(self, tree, location)

    def plant_trees(self, plants: list[tuple[Tree, tuple[Decimal, Decimal]]]):
        """Plant multiple trees."""

        for tree, location in plants:
            self.plant_tree(tree, location)


class UserAccount(models.Model):
    """Relationship between User and Account."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "account")


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
