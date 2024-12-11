from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Account, User, Profile
from accounts.models import PlantedTree

class AccountAdmin(admin.ModelAdmin):
    """
    Interface admin to manage the Account model.
    """
    list_display = ('name', 'created', 'active')
    list_filter = ('active',)
    actions = ['activate_accounts', 'deactivate_accounts']

    def activate_accounts(self, request, queryset):
        queryset.update(active=True)
    activate_accounts.short_description = "Ativar contas selecionadas"

    def deactivate_accounts(self, request, queryset):
        queryset.update(active=False)
    deactivate_accounts.short_description = "Desativar contas selecionadas"

class UserAdmin(BaseUserAdmin):
    """
    Interface admin to manage the User model.
    """
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    filter_horizontal = ('accounts',)


class PlantedTreeAdmin(admin.ModelAdmin):
    """
    Interface admin to manage the PlantedTree model.
    """
    list_display = ('tree', 'user', 'account', 'age', 'location', 'planted_at')  


admin.site.register(Account, AccountAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Profile)
admin.site.register(PlantedTree, PlantedTreeAdmin)