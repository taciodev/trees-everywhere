from django.contrib import admin
from .models import Account, User, Profile, PlantedTree
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class AccountAdmin(admin.ModelAdmin):
    """
    Interface administrativa para gerenciar o modelo Account.
    Permite ativar e desativar contas em massa.
    """
    list_display = ('name', 'created', 'active')
    list_filter = ('active',)
    actions = ['activate_accounts', 'deactivate_accounts']

    def activate_accounts(self, request, queryset):
        """Ativa as contas selecionadas."""
        queryset.update(active=True)
    activate_accounts.short_description = "Ativar contas selecionadas"

    def deactivate_accounts(self, request, queryset):
        """Desativa as contas selecionadas."""
        queryset.update(active=False)
    deactivate_accounts.short_description = "Desativar contas selecionadas"

class UserAdmin(BaseUserAdmin):
    """
    Interface administrativa para gerenciar o modelo User.
    Permite associar usuários a contas usando um filtro horizontal.
    """
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    filter_horizontal = ('accounts',)


class PlantedTreeAdmin(admin.ModelAdmin):
    """
    Interface administrativa para gerenciar o modelo PlantedTree.
    """
    list_display = ('tree', 'user', 'account', 'age', 'location', 'planted_at')  # Defina os campos a serem exibidos na lista
    # Adicione outros campos ou funcionalidades conforme necessário


# Registra os modelos no admin
admin.site.register(Account, AccountAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Profile)
admin.site.register(PlantedTree, PlantedTreeAdmin)  # Registre o modelo com a classe admin
