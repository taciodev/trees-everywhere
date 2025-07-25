from django import forms
from django.contrib.auth import get_user_model

from accounts.models import Account, PlantedTree, UserAccount

User = get_user_model()

class PlantedTreeForm(forms.ModelForm):
    class Meta:
        model = PlantedTree
        fields = ['tree', 'age', 'account']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user_id = self.initial.get('user')
        if user_id:
            user_accounts = UserAccount.objects.filter(user_id=user_id).values_list('account', flat=True)
            self.fields['account'].queryset = Account.objects.filter(id__in=user_accounts)