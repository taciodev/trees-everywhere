from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    """
    Represents a user account, with information
    """
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Conta'
        verbose_name_plural = 'Contas'

    def __str__(self):
        return self.name


class UserAccount(models.Model):
    """
    Represents the link between a user and an account.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_accounts')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='account_users')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'account'], name='unique_user_account')
        ]
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.user.username
