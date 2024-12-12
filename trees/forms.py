from django import forms
from .models import Tree
from accounts.models import Account, PlantedTree

class PlantedTreeForm(forms.ModelForm):
    class Meta:
        model = PlantedTree
        fields = ['tree', 'age', 'location', 'account']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tree'].queryset = Tree.objects.all()
        self.fields['account'].queryset = Account.objects.all()