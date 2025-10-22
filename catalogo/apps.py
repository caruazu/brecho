from django.apps import AppConfig

class CatalogoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'catalogo'

    def ready(self):
        from django.db.models.signals import post_migrate
        from django.apps import apps as global_apps
        from django.conf import settings
        from decimal import Decimal

        def seed_items(sender, **kwargs):
            # opcional: só semear em DEV
            if not getattr(settings, "DEBUG", True):
                return

            Item = global_apps.get_model("catalogo", "Item")
            if Item.objects.exists():
                return  # evita duplicar

            Item.objects.bulk_create([
                Item(nome="blusinha",  preco=Decimal("10.00"), estoque=1, disponivel=True),
                Item(nome="calcinha",  preco=Decimal("5.00"),  estoque=1, disponivel=True),
                Item(nome="shortinho", preco=Decimal("15.00"), estoque=1, disponivel=True),
            ])

        # conecta o sinal só para este app
        post_migrate.connect(seed_items, sender=self)