from django.contrib import admin
from .models import InvoiceEntry, InvoiceEntryItem

# Register your models here.


class InvoiceEntryItemAdmin(admin.TabularInline):
    model = InvoiceEntryItem
    raw_id_fields = ('p_id',)


@admin.register(InvoiceEntry)
class InvoiceEntryAdmin(admin.ModelAdmin):
    list_display = ['u_wholesaler_id', 'ie_driver', 'ie_total_weight', 'ie_date_time']
    inlines = (InvoiceEntryItemAdmin,)
