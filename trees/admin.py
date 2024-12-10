from django.contrib import admin
from .models import Tree, PlantedTree


class TreeAdmin(admin.ModelAdmin):
    """
    Customize the administrative interface for the Tree model.
    """
    list_display = ('name', 'scientific_name')
    search_fields = ('name',)


admin.site.register(Tree, TreeAdmin)


# TODO: LISTAR APENAS AS CONTAS DO USUÁRIO LOGADO
class PlantedTreeAdmin(admin.ModelAdmin):
    """
    Customizes the administrative interface for the TreeType model.
    """
    list_display = ('age', 'planted_at', 'tree', 'user', 'account')
    search_fields = ('tree', 'user')
    list_filter = ('tree',)


admin.site.register(PlantedTree, PlantedTreeAdmin)