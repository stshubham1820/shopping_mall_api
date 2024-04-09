from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _
import contextlib

class ProductBillingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = "shopping_mall.product_billing"
    verbose_name = _("ProductBilling")
