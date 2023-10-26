from rest_framework import serializers

from . import models
from product.serializers import ProductSerializer
from user.models import UserGroupOrganization


class InvoiceEntryAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InvoiceEntry
        fields = '__all__'


class InvoiceEntryItemAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InvoiceEntryItem
        fields = '__all__'


class UserInvoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserGroupOrganization


class InvoiceEntrySerializer(serializers.ModelSerializer):
    wholesaler_id = UserInvoiceSerializer(read_only=True)

    class Meta:
        model = models.InvoiceEntry
        fields = ['id',
                  'wholesaler_id',
                  'ie_driver',
                  'full_weight',
                  'empty_weight',
                  'created_at']


class InvoiceEntryItemSerializer(serializers.ModelSerializer):
    p_id = ProductSerializer()

    class Meta:
        model = models.InvoiceEntryItem
        fields = ['id', 'invoice_entry_id', 'product_id', 'weight']