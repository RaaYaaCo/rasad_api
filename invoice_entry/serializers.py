from rest_framework import serializers

from . import models
from product.serializers import ProductSerializer
from user.serializers import UgoSerializer


class InvoiceEntryAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InvoiceEntry
        fields = '__all__'


class InvoiceEntryItemAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InvoiceEntryItem
        fields = '__all__'


class InvoiceEntrySerializer(serializers.ModelSerializer):
    wholesaler_id = UgoSerializer(read_only=True, many=True)

    class Meta:
        model = models.InvoiceEntry
        fields = ['id',
                  'wholesaler_id',
                  'driver',
                  'full_weight',
                  'empty_weight',
                  'created_at']


class InvoiceEntryItemSerializer(serializers.ModelSerializer):
    product_id = ProductSerializer(read_only=True)

    class Meta:
        model = models.InvoiceEntryItem
        fields = ['id', 'invoice_entry_id', 'product_id', 'weight']
