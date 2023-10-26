from django.contrib import admin
from .models import InvoiceSales, InvoiceSalesItem

# Register your models here.


class InvoiceSalesItemAdmin(admin.TabularInline):
    model = InvoiceSalesItem
    raw_id_fields = ('product_price_id',)  # ?


@admin.register(InvoiceSales)
class InvoiceSalesAdmin(admin.ModelAdmin):
    list_display = ['wholesaler_ugo', 'store_ugo', 'created_at']
    inlines = (InvoiceSalesItemAdmin,)
