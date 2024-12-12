from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model

from trees.models import Tree


class Account(models.Model):
    """A model to represent an account in the system."""

    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    """A custom user model that extends the AbstractUser model."""
    accounts = models.ManyToManyField('Account', related_name='users')


    def plant_tree(self, tree, location):
        """Plant a tree for the user."""

        PlantedTree.objects.create(
            user=self,
            tree=tree,
            location=location
        )

    def plant_trees(self, plants):
        """Plant multiple trees for the user."""

        for tree, location in plants:
            self.plant_tree(tree, location)


class UserAccount(models.Model):
    """Relationship between User and Account."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'account')


class Profile(models.Model):
    """A model to represent a user profile."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField(blank=True)
    joined = models.DateTimeField(auto_now_add=True)


class PlantedTree(models.Model):
    """A model to represent a tree planted by a user."""

    age = models.IntegerField(default=0)
    planted_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tree = models.ForeignKey(Tree, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.tree.name} plantada por {self.user.username} em {self.planted_at}"