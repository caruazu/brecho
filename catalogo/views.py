from django.views.generic import ListView
from catalogo.models import Item

class Home(ListView):
    model = Item
    template_name = "catalogo/home.html"
    context_object_name = "itens"

    def gey_queryset(self):
        return Item.objects.filter(disponivel=True).order_by("nome")
