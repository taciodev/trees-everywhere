from django.contrib import admin
from django.contrib.auth import forms
from django.contrib.auth.models import User

from .models import Account, UserAccount


class CustomUserCreationForm(forms.UserCreationForm):
    """
    User creation form with additional fields.
    """
    class Meta(forms.UserCreationForm.Meta):
        model = User
        fields = forms.UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        """
        Adds 'form-control' class to fields.
        """
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class UserAccountInline(admin.TabularInline):
    """
    Inline to associate users with accounts in Admin.
    """
    model = UserAccount
    extra = 1


class AccountAdmin(admin.ModelAdmin):
    """
    Custom display of Account model in Admin.
    """
    list_display = ('name', 'created', 'active')
    inlines = [UserAccountInline]


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    """
    Registers the Account model in the Admin.
    """
    list_display = ('name', 'created', 'active')
    inlines = [UserAccountInline]
