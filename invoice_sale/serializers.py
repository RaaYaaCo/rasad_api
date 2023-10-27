from rest_framework import serializers

from .models import InvoiceSales, InvoiceSalesItem
from user.serializers import UgoSerializer
from product.serializers import ProductSerializer, ProductPriceSerializer
# from store.serializers import StoreSerializer


class InvoiceSalesAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceSales
        fields = '__all__'


class InvoiceSalesItemAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceSalesItem
        fields = '__all__'


class InvoiceSalesSerializer(serializers.ModelSerializer):
    wholesaler_ugo = UgoSerializer(read_only=True)
    store_ugo = UgoSerializer(read_only=True)

    class Meta:
        model = InvoiceSales
        fields = ['id',
                  'wholesaler_ugo',
                  'store_ugo',
                  'created_at'
                  ]


class InvoiceSalesItemSerializer(serializers.ModelSerializer):
    product_id = ProductSerializer(read_only=True)
    product_price_id = ProductPriceSerializer(read_only=True)

    class Meta:
        model = InvoiceSalesItem
        fields = ['id', 'invoice_sales_id', 'product_id', 'weight', 'product_price_id']
