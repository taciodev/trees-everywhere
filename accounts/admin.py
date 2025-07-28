from django.contrib import admin
from .models import Account, UserAccount


class UserAccountInline(admin.TabularInline):
    model = UserAccount
    extra = 1
    autocomplete_fields = ["user"]


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    """Interface admin to manage the Account model."""

    list_display = ("name", "created", "active")
    list_filter = ("active",)
    search_fields = ("name",)
    inlines = [UserAccountInline]
    actions = ["activate_accounts", "deactivate_accounts"]

    def activate_accounts(self, request, queryset):
        queryset.update(active=True)

    activate_accounts.short_description = "Ativar contas selecionadas"

    def deactivate_accounts(self, request, queryset):
        queryset.update(active=False)

    deactivate_accounts.short_description = "Desativar contas selecionadas"
