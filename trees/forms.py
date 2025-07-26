from django import forms
from django.contrib.auth import get_user_model

from accounts.models import Account, UserAccount
from .models import PlantedTree

User = get_user_model()


class PlantedTreeForm(forms.ModelForm):
    class Meta:
        model = PlantedTree
        fields = ["tree", "age", "account", "latitude", "longitude"]
        widgets = {
            "tree": forms.Select(attrs={"class": "form-select"}),
            "age": forms.NumberInput(attrs={"class": "form-control", "min": "0"}),
            "account": forms.Select(attrs={"class": "form-select"}),
            "latitude": forms.NumberInput(
                attrs={"class": "form-control", "step": "0.000001"}
            ),
            "longitude": forms.NumberInput(
                attrs={"class": "form-control", "step": "0.000001"}
            ),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)  # Melhor que usar self.initial
        super().__init__(*args, **kwargs)

        if user:
            user_accounts = UserAccount.objects.filter(user=user).values_list(
                "account", flat=True
            )
            self.fields["account"].queryset = Account.objects.filter(
                id__in=user_accounts
            )
