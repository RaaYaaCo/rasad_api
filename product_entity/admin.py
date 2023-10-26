from django.contrib import admin
from .models import ProductEntity

# Register your models here.


@admin.register(ProductEntity)
class ProductEntityAdmin(admin.ModelAdmin):
    list_display = ['store_ugo', 'invoice_sales_item_id', 'product_id', 'sale_price', 'is_active']
