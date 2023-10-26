from rest_framework.generics import GenericAPIView, RetrieveAPIView, ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from utils.translate import translate
from .models import InvoiceSales, InvoiceSalesItem
from product_entity.models import ProductEntity
from .serializers import InvoiceSalesAddSerializer, InvoiceSalesItemAddSerializer
from product.models import ProductPrice
# from .serializers import InvoiceSalesSerializer,\
#     InvoiceSalesAddSerializer,\
#     # InvoiceSalesItemSerializer,\
#     # InvoiceSalesItemAddSerializer
# from invoice_customer.models import ProductEntity

# Create your views here.


class InvoiceSalesAddView(GenericAPIView):
    serializer_class = InvoiceSalesAddSerializer
    queryset = InvoiceSales.objects.all()

    def post(self, request: Request) -> Response:
        translate(request)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data,
                        status=status.HTTP_201_CREATED)


class InvoiceSalesItemAddView(GenericAPIView):
    serializer_class = InvoiceSalesItemAddSerializer
    queryset = InvoiceSales.objects.all()

    def post(self, request: Request) -> Response:
        translate(request)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        invoice = InvoiceSales.objects.get(id=serializer.data['invoice_sales_id'])
        product_price = ProductPrice.objects.get(id=serializer.data['product_price_id'])
        price = product_price.price + (product_price.price * 0.3)
        ProductEntity.objects.create(
            store_ugo_id=invoice.store_ugo.id,
            # u_store_id_id=invoice.u_store_id.id,
            invoice_sales_item_id_id=invoice.id,
            # isi_id_id=invoice.id,
            product_id_id=serializer.data['product_price_id'],
            # p_id_id=serializer.data['p_id'],
            invoice_sales_item_price=price,
            # isi_price=price,
            sale_price=price,
            # sale_price=price,
            weight=serializer.data['weight'],
            # pe_weight=serializer.data['isi_weight'],
        )
        return Response(data=serializer.data,
                        status=status.HTTP_201_CREATED)


# class InvoiceSalesShowAllView(ListAPIView):
#     serializer_class = InvoiceSalesSerializer
#     queryset = InvoiceSales.objects.all().order_by('-is_date_time')
#     filterset_fields = ['u_wholesaler_id', 'u_store_id', 'is_date_time']
#
#
# class InvoiceSalesShowDetailView(RetrieveAPIView):
#     serializer_class = InvoiceSalesSerializer
#     queryset = InvoiceSales.objects.all()
#
#     def retrieve(self, request: Request, *args, **kwargs):
#         translate(request)
#         instance = self.get_object()
#         serializer = self.serializer_class(instance)
#         item_instance = InvoiceSalesItem.objects.filter(is_id_id=serializer.data['id'])
#         item_serializer = InvoiceSalesItemSerializer(item_instance, many=True)
#         return Response({'invoice': serializer.data, 'items': item_serializer.data}, status.HTTP_200_OK)
#
#
# class InvoiceSalesShowDetailWholesalerView(GenericAPIView):
#     serializer_class = InvoiceSalesSerializer
#     queryset = InvoiceSales.objects.all()
#     lookup_field = 'u_wholesaler_id'
#
#     def get(self, request: Request, *args, **kwargs):
#         translate(request)
#         invoice_entry = InvoiceSales.objects.filter(u_wholesaler_id_id=self.kwargs['u_wholesaler_id'])
#         serializer = self.serializer_class(invoice_entry, many=True)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#
# class InvoiceSalesShowDetailStoreView(GenericAPIView):
#     serializer_class = InvoiceSalesSerializer
#     queryset = InvoiceSales.objects.all()
#     lookup_field = 'u_store_id'
#
#     def get(self, request: Request, *args, **kwargs):
#         translate(request)
#         invoice_entry = InvoiceSales.objects.filter(u_store_id_id=self.kwargs['u_store_id'])
#         serializer = self.serializer_class(invoice_entry, many=True)
#         return Response(serializer.data, status.HTTP_200_OK)
