from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Account, User, Profile, UserAccount, PlantedTree


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    """Interface admin to manage the Account model."""

    list_display = ('name', 'created', 'active')
    list_filter = ('active',)
    search_fields = ('name',)
    actions = ['activate_accounts', 'deactivate_accounts']

    def activate_accounts(self, request, queryset):
        queryset.update(active=True)
    activate_accounts.short_description = "Ativar contas selecionadas"

    def deactivate_accounts(self, request, queryset):
        queryset.update(active=False)
    deactivate_accounts.short_description = "Desativar contas selecionadas"


class UserAccountInline(admin.TabularInline):
    """Relationship between User and Account."""

    model = UserAccount
    extra = 1


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Interface admin to manage the User model."""

    list_display = ('username', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    search_fields = ('username', 'email')
    
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Datas importantes', {'fields': ('last_login', 'date_joined')}),
    )
    readonly_fields = ('last_login', 'date_joined')
    
    inlines = (UserAccountInline,)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Interface admin to manage the Profile model."""

    list_display = ('user',)
    search_fields = ('user__username',)


@admin.register(PlantedTree)
class PlantedTreeAdmin(admin.ModelAdmin):
    """Interface admin to manage the PlantedTree model."""

    list_display = ('tree', 'user', 'account', 'age', 'planted_at', 'get_location')
    search_fields = ('tree__name', 'user__username', 'account__name')

    def get_location(self, obj):
        return obj.location
    get_location.short_description = 'Localização'