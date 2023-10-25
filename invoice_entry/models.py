from django.db import models
from django.utils.translation import gettext as _

from user.models import UserGroupOrganization
from product.models import Product


class InvoiceEntry(models.Model):
    wholesaler_id = models.ForeignKey(UserGroupOrganization,
                                      on_delete=models.PROTECT,
                                      db_index=True,
                                      verbose_name=_('wholesaler'))
    driver = models.CharField(max_length=15,
                              verbose_name=_('driver'))
    full_weight = models.FloatField(verbose_name=_('full weight'))
    empty_weight = models.FloatField(verbose_name=_('empty name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return f'{self.wholesaler_id.o_id.name} | {self.created_at}'

    def save(self, *args, **kwargs):
        if self.wholesaler_id.g_id.name != 'عمده فروش':
            raise _('your request can not accept')
        else:
            return super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('invoice entry')
        verbose_name_plural = _('invoice entries')


class InvoiceEntryItem(models.Model):
    invoice_entry_id = models.ForeignKey(InvoiceEntry, on_delete=models.PROTECT, verbose_name=_('invoice_entry_id'))
    product_id = models.ForeignKey(Product.slug, on_delete=models.PROTECT, verbose_name=_('product slug'))
    weight = models.FloatField(verbose_name=_('weight'))

    def __str__(self):
        return f'{self.invoice_entry_id.wholesaler_id.o_id.name} | {self.product_id} | {self.weight}'

    class Meta:
        verbose_name = _('invoice entry item')
        verbose_name_plural = _('invoice entry items')
