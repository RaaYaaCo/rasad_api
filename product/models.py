from django.db import models
from django.utils.translation import gettext as _


class ProductType(models.Model):
    pt_title = models.CharField(max_length=100, verbose_name=_('title'), unique=True, db_index=True)

    def __str__(self):
        return self.pt_title

    class Meta:
        verbose_name = _('Product Type')
        verbose_name_plural = _('Products Type')


class Degree(models.Model):
    d_title = models.CharField(max_length=100, verbose_name=_('title'), unique=True, db_index=True)

    def __str__(self):
        return self.d_title

    class Meta:
        verbose_name = _('Degree')
        verbose_name_plural = _('Degrees')


class Unit(models.Model):
    un_title = models.CharField(max_length=100, verbose_name=_('title'), unique=True, db_index=True)

    def __str__(self):
        return self.un_title

    class Meta:
        verbose_name = _('Unit')
        verbose_name_plural = _('Units')


class Product(models.Model):
    p_name = models.CharField(max_length=100, db_index=True, verbose_name=_('name'))
    P_description = models.TextField(verbose_name=_('description'), blank=True, null=True),
    image = models.ImageField(upload_to='product/images/', verbose_name='image', blank=True, null=True)
    pt_id = models.ForeignKey(ProductType, on_delete=models.PROTECT, verbose_name=_('product type'), db_index=True)
    d_id = models.ForeignKey(Degree, on_delete=models.PROTECT, verbose_name=_('degree'), db_index=True)
    un_id = models.ForeignKey(Unit, on_delete=models.PROTECT, default=1, verbose_name=_('Unit'))
    p_slug = models.CharField(max_length=100, db_index=True, verbose_name=_('slug'), unique=True, blank=True)

    def __str__(self):
        return f'{self.p_name} / {self.d_id}'

    def save(self, *args, **kwargs):
        slug = self.p_name + '-' + self.d_id.d_title
        self.p_slug = slug.replace(' ', '-')
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class ProductPrice(models.Model):
    p_id = models.ForeignKey(Product, on_delete=models.PROTECT, db_index=True, verbose_name=_('product'))
    pp_price = models.PositiveIntegerField(db_index=True, verbose_name=_('price'))
    pp_is_active = models.BooleanField(default=True, verbose_name=_('is active'))
    pp_date_time = models.DateTimeField(auto_now_add=True, verbose_name=_('date and time'))
    pp_update_time = models.DateTimeField(auto_now=True, verbose_name=_('update time'))

    def __str__(self):
        return f'{self.p_id} / {self.pp_price}'

    class Meta:
        verbose_name = _('Product price')
        verbose_name_plural = _('Products price')
