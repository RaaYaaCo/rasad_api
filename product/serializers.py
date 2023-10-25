from rest_framework import serializers
from .models import ProductType, Unit, Degree, Product, ProductPrice


class ProductTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'


class UnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Unit
        fields = '__all__'


class DegreeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Degree
        fields = '__all__'


class ProductSerializers(serializers.ModelSerializer):
    pt_id = ProductTypeSerializers(read_only=True)
    d_id = DegreeSerializer(read_only=True)
    un_id = UnitSerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['p_slug']


class ProductAddSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['slug']


class ProductPriceSerializer(serializers.ModelSerializer):
    p_id = ProductSerializers(read_only=True)

    class Meta:
        model = ProductPrice
        fields = '__all__'
        read_only_fields = ['is_active']


class ProductPriceAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPrice
        fields = '__all__'
        read_only_fields = ['is_active']
