from django.contrib import admin
from .models import Tree, PlantedTree


class PlantedTreeInline(admin.TabularInline):
    """
    Inline edition of PlantedTree instances.
    """

    model = PlantedTree
    extra = 0
    fields = ("user", "account")
    readonly_fields = ("user", "account")


@admin.register(Tree)
class TreeAdmin(admin.ModelAdmin):
    """
    Admin page for Tree instances.
    """

    inlines = [PlantedTreeInline]

    def planted_trees(self, obj):
        return ", ".join([pt.user.username for pt in obj.plantedtree_set.all()])

    planted_trees.short_description = "Plantadas por"


@admin.register(PlantedTree)
class PlantedTreeAdmin(admin.ModelAdmin):
    """Interface admin to manage the PlantedTree model."""

    list_display = ("tree", "user", "account", "age", "planted_at", "get_location")
    search_fields = ("tree__name", "user__username", "account__name")

    def get_location(self, obj):
        return obj.location

    get_location.short_description = "Localização"
