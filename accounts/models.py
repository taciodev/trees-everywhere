from decimal import Decimal
from django.db import models
from django.contrib.auth.models import AbstractUser
from trees.models import Tree


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

        PlantedTree.objects.create(user=self, tree=tree, location=location)

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


class PlantedTree(models.Model):
    """A model to represent a tree planted by a user."""

    age = models.IntegerField(default=0)
    planted_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tree = models.ForeignKey(Tree, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, default=Decimal("0.0")
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, default=Decimal("0.0")
    )

    class Meta:
        verbose_name = "Árvore Plantada"
        verbose_name_plural = "Árvores Plantadas"

    @property
    def location(self):
        return (self.latitude, self.longitude)

    def __str__(self):
        return (
            f"{self.tree.name} plantada por {self.user.username} em {self.planted_at}"
        )
