from django.db import models
from accounts.models import Account, UserAccount


class Tree(models.Model):
    """
    Represents the types of trees available.
    """
    name = models.CharField(max_length=255)
    scientific_name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Tree'
        verbose_name_plural = 'Tree'

    def __str__(self):
        return self.name


class PlantedTree(models.Model):
    """
    Represents a planted tree, with name, type and characteristics.
    """
    age = models.IntegerField()
    planted_at = models.DateTimeField(auto_now_add=True)
    tree = models.ForeignKey(Tree, on_delete=models.CASCADE)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Planted Tree'
        verbose_name_plural = 'Planted Trees'

    def __str__(self):
        return self.tree.name
