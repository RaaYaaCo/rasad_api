from django.db import models
from django.utils.translation import gettext as _

from product.models import Product, ProductPrice
from user.models import UserGroupOrganization

# Create your models here.


class InvoiceSales(models.Model):
    wholesaler_ugo = models.ForeignKey(UserGroupOrganization,
                                       on_delete=models.PROTECT,
                                       db_index=True,
                                       verbose_name=_('wholesaler'),
                                       related_name='wholesalerSales')
    store_ugo = models.ForeignKey(UserGroupOrganization,
                                  on_delete=models.PROTECT,
                                  db_index=True,
                                  verbose_name=_('store'),
                                  related_name='storeSales')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('date time'))

    def __str__(self):
        return f'{self.wholesaler_ugo.o_id.name} / {self.store_ugo.o_id.name}'

    class Meta:
        verbose_name = _('Invoice Sales')
        verbose_name_plural = _('Invoices Sales')


class InvoiceSalesItem(models.Model):
    invoice_sales_id = models.ForeignKey(InvoiceSales,
                                         on_delete=models.CASCADE,
                                         db_index=True,
                                         verbose_name=_('Invoice'))
    product_id = models.ForeignKey(Product,
                                   on_delete=models.PROTECT,
                                   db_index=True,
                                   verbose_name=_('product'))
    product_price_id = models.ForeignKey(ProductPrice,
                                         on_delete=models.CASCADE,
                                         db_index=True,
                                         verbose_name=_('product price'))
    weight = models.FloatField(verbose_name=_('weight'))

    def __str__(self):
        return f'{self.invoice_sales_id.store_ugo.o_id.name} / {self.product_price_id.product_id.name}'

    class Meta:
        verbose_name = _('Invoice Sales Item')
        verbose_name_plural = 'Invoice Sales Item'
