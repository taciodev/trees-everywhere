from django.db import models


class Tree(models.Model):
    name = models.CharField(max_length=255)
    scientific_name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Árvore"
        verbose_name_plural = "Árvores"

    def __str__(self):
        return self.name


class PlantedTree(models.Model):
    """A model to represent a tree planted by a user."""

    age = models.IntegerField(default=0)
    planted_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    tree = models.ForeignKey(Tree, on_delete=models.CASCADE)
    account = models.ForeignKey("accounts.Account", on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default="0.0")
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default="0.0")

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
