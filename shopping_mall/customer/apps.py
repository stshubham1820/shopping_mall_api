from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CustomerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = "shopping_mall.customer"
    verbose_name = _("Customers")
