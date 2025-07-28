from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.models import UserAccount
from .models import User, Profile


class ReadOnlyUserAccountInline(admin.TabularInline):
    model = UserAccount
    extra = 0
    can_delete = False
    verbose_name = "Conta"
    verbose_name_plural = "Contas"
    fields = ("account",)
    readonly_fields = ("account",)
    show_change_link = False


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Interface admin to manage the User model."""

    list_display = ("username", "email", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active", "is_superuser")
    search_fields = ("username", "email")
    inlines = [ReadOnlyUserAccountInline]

    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        ("Permissões", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Datas importantes", {"fields": ("last_login", "date_joined")}),
    )
    readonly_fields = ("last_login", "date_joined")


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Interface admin to manage the Profile model."""

    list_display = ("user",)
    search_fields = ("user__username",)
