from rest_framework import serializers

from . import models
from product.serializers import ProductSerializer


class InvoiceEntryAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InvoiceEntry
        fields = '__all__'


class InvoiceEntryItemAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InvoiceEntryItem
        fields = '__all__'


class InvoiceEntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.InvoiceEntry
        fields = ['id',
                  'wholesaler_id',
                  'driver',
                  'full_weight',
                  'empty_weight',
                  'created_at']


class InvoiceEntryItemSerializer(serializers.ModelSerializer):
    p_id = ProductSerializer()

    class Meta:
        model = models.InvoiceEntryItem
        fields = ['id', 'invoice_entry_id', 'product_id', 'weight']
