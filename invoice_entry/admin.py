from django.contrib import admin
from .models import InvoiceEntry, InvoiceEntryItem

# Register your models here.


class InvoiceEntryItemAdmin(admin.TabularInline):
    model = InvoiceEntryItem
    raw_id_fields = ('product_id',)


@admin.register(InvoiceEntry)
class InvoiceEntryAdmin(admin.ModelAdmin):
    list_display = ['wholesaler_id', 'driver', 'created_at']
    inlines = (InvoiceEntryItemAdmin,)
