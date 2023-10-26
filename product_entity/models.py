from django.db import models
from django.utils.translation import gettext as _

from invoice_sale.models import InvoiceSales
from product.models import Product
from user.models import UserGroupOrganization
# Create your models here.


class ProductEntity(models.Model):
    store_ugo = models.ForeignKey(UserGroupOrganization,
                                  on_delete=models.PROTECT,
                                  db_index=True,
                                  verbose_name=_('store'),
                                  related_name='storeProductEntity')
    invoice_sales_item_id = models.ForeignKey(InvoiceSales,
                                              on_delete=models.PROTECT,
                                              db_index=True,
                                              verbose_name=_('Invoice Sales'))
    product_id = models.ForeignKey(Product,
                                   on_delete=models.PROTECT,
                                   verbose_name=_('product'))
    invoice_sales_item_price = models.PositiveIntegerField(verbose_name=_('Invoice Sales price'))
    sale_price = models.PositiveIntegerField(verbose_name=_('sale price'))
    weight = models.PositiveIntegerField(verbose_name=_('weight'))
    is_active = models.BooleanField(default=True, verbose_name=_('active/deactivate'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('date time'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('update time'))

    def __str__(self):
        return f'{self.store_ugo.o_id.name} / {self.product_id.name} / {self.sale_price}'

    class Meta:
        verbose_name = _('Product Entity')
        verbose_name_plural = _('Products Entity')
