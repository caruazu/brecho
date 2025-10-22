from django.contrib import admin

from catalogo.models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco", "estoque", "disponivel")
    list_filter = ("disponivel",)
    search_fields = ("nome",)