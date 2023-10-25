from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext as _

from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from core.utils import translate
from .serializers import ProductTypeSerializers, UnitSerializer, \
    DegreeSerializer, ProductSerializers, ProductPriceSerializer, \
    ProductAddSerializers, ProductPriceAddSerializer
from .models import ProductType, Degree, Unit, Product, ProductPrice


class ProductTypeView(generics.CreateAPIView):
    serializer_class = ProductTypeSerializers
    queryset = ProductType.objects.all()

    def create(self, request: Request, *args, **kwargs):
        translate(Request)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data={'data': serializer.data, 'msg': _('you select the product type successfully')},
                        status=status.HTTP_201_CREATED)


class ProductTypeDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = ProductTypeSerializers
    queryset = ProductType.objects.all()

    def retrieve(self, request, *args, **kwargs):
        translate(request)
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        return Response(serializer.data, status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        translate(request)
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)


class DegreeView(generics.CreateAPIView):
    serializer_class = DegreeSerializer
    queryset = Degree.objects.all()

    def create(self, request: Request, *args, **kwargs):
        translate(Request)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data={'data': serializer.data, 'msg': _('you add degree successfully')},
                        status=status.HTTP_201_CREATED)


class DegreeDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = DegreeSerializer
    queryset = Degree.objects.all()

    def retrieve(self, request, *args, **kwargs):
        translate(request)
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        return Response(serializer.data, status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        translate(request)
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)


class UnitView(generics.CreateAPIView):
    serializer_class = UnitSerializer
    queryset = Unit.objects.all()

    def create(self, request: Request, *args, **kwargs):
        translate(Request)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data={'data': serializer.data, 'msg': _('you add unit successfully')},
                        status=status.HTTP_201_CREATED)


class UnitDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = UnitSerializer
    queryset = Unit.objects.all()

    def retrieve(self, request, *args, **kwargs):
        translate(request)
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        return Response(serializer.data, status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        translate(request)
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    filterset_fields = ['p_name', 'pt_id', 'd_id']


class ProductAddView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductAddSerializers

    def create(self, request: Request, *args, **kwargs):
        translate(request)
        serializer = ProductAddSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response({'msg': _('you can not register a product with the same name and degree')})


class ProductDetailView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductAddSerializers
    lookup_field = "p_slug"

    def retrieve(self, request: Request, *args, **kwargs):
        translate(request)
        instance = self.get_object()
        serializer = ProductSerializers(instance)
        return Response(serializer.data, status.HTTP_200_OK)

    def update(self, request: Request, *args, **kwargs):
        translate(request)
        instance = self.get_object()
        serializer = ProductAddSerializers(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response({'msg': _('you can not register a product with the same name and degree')})


class ProductPriceView(generics.ListAPIView):
    serializer_class = ProductPriceSerializer
    queryset = ProductPrice.objects.filter(pp_is_active=True)
    filterset_fields = ['p_id', 'pp_price']


class ProductPriceAddView(generics.GenericAPIView):
    serializer_class = ProductPriceAddSerializer
    queryset = ProductPrice.objects.all()

    def post(self, request: Request):
        translate(request)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                previous_product_price = ProductPrice.objects.get(p_id=request.data['p_id'],
                                                                  pp_is_active=True)
                previous_product_price.pp_is_active = False
                previous_product_price.save()
                serializer.save()
                return Response(data={'data': serializer.data, 'msg': _('new price registered')},
                                status=status.HTTP_201_CREATED)

            except ObjectDoesNotExist:
                serializer.save()
                return Response(data={'data': serializer.data, 'msg': _('new price registered')},
                                status=status.HTTP_201_CREATED)


class EachProductPriceView(generics.GenericAPIView):
    serializer_class = ProductPriceSerializer
    queryset = ProductPrice.objects.filter
    lookup_field = 'p_id'

    def get(self, request: Request, *args, **kwargs):
        translate(request)
        instance = self.queryset(p_id=self.kwargs['p_id']).order_by('-pp_date_time')
        serializer = self.serializer_class(instance, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
