from django.contrib import admin
from . import models


@admin.register(models.InvoiceEntry)
class InvoiceEntryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.InvoiceEntryItem)
class InvoiceEntryItemAdmin(admin.ModelAdmin):
    pass
