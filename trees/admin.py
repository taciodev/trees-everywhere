from django.contrib import admin
from .models import Tree, PlantedTree


class TreeAdmin(admin.ModelAdmin):
    """
    Customize the admin interface for Tree model.
    """
    list_display = ('name', 'scientific_name')
    search_fields = ('name',)


admin.site.register(Tree, TreeAdmin)


class PlantedTreeAdmin(admin.ModelAdmin):
    """
    Customize the admin interface for PlantedTree model.
    """
    list_display = ('age', 'planted_at', 'tree', 'user', 'account')
    search_fields = ('tree', 'user')
    list_filter = ('tree',)

    # TODO: LISTAR APENAS AS CONTAS DO USUÁRIO LOGADO


admin.site.register(PlantedTree, PlantedTreeAdmin)
