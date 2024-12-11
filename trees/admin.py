from django.contrib import admin
from .models import Tree
from accounts.models import PlantedTree


class PlantedTreeInline(admin.TabularInline):
    """
    Inline edition of PlantedTree instances.
    """
    model = PlantedTree
    extra = 1
    readonly_fields = ('user', 'account')


class TreeAdmin(admin.ModelAdmin):
    """
    Admin page for Tree instances.
    """
    inlines = [PlantedTreeInline]
    def planted_trees(self, obj):
        return ", ".join([pt.user.username for pt in obj.plantedtree_set.all()])
    planted_trees.short_description = 'Plantadas por'


admin.site.register(Tree, TreeAdmin)
