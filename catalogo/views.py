from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from catalogo.models import Item

class Home(ListView):
    model = Item
    template_name = "catalogo/home.html"
    context_object_name = "itens"

    def gey_queryset(self):
        return Item.objects.filter(disponivel=True).order_by("nome")

@require_POST
def toggle_disponivel(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.disponivel = not item.disponivel
    item.save(update_fields=["disponivel"])
    return JsonResponse({"id": item.id, "disponivel": item.disponivel})