from rest_framework import serializers
from . import models


class InvoiceEntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.InvoiceEntry
        fields = '__all__'


class InvoiceEntryAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InvoiceEntry
        fields = '__all__'


class InvoiceEntryItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.InvoiceEntryItem
        fields = '__all__'


class InvoiceEntryItemAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InvoiceEntryItem
        fields = '__all__'
