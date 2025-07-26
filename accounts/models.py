from django.db import models
from users.models import User


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


class UserAccount(models.Model):
    """Relationship between User and Account."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "account")
