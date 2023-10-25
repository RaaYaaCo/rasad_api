from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    pass


@admin.register(Degree)
class DegreeAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class Product(admin.ModelAdmin):
    pass


@admin.register(ProductPrice)
class ProductPriceAdmin(admin.ModelAdmin):
    pass
