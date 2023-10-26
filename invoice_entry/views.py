from django.utils.translation import gettext as _
from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from utils.translate import translate
from . import serializers
from . import models


class InvoiceEntryAddView(generics.GenericAPIView):
    serializer_class = serializers.InvoiceEntryAddSerializer
    queryset = models.InvoiceEntry.objects.all()

    def post(self, request: Request):
        translate(request)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class InvoiceEntryItemAddView(generics.GenericAPIView):
    serializer_class = serializers.InvoiceEntryItemAddSerializer
    queryset = models.InvoiceEntryItem.objects.all()

    def post(self, request: Request):
        translate(request)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class InvoiceEntryShowAllView(generics.ListAPIView):
    serializer_class = serializers.InvoiceEntrySerializer
    queryset = models.InvoiceEntry.objects.all().order_by('-created_at')
    filterset_fields = ['wholesaler_id', 'created_at']


class InvoiceEntryShowDetailView(generics.RetrieveAPIView):
    serializer_class = serializers.InvoiceEntrySerializer
    queryset = models.InvoiceEntry.objects.all()

    def retrieve(self, request: Request, *args, **kwargs):
        translate(request)
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        item_instance = models.InvoiceEntryItem.objects.filter(invoice_entry_id_id=serializer.data['id'])
        item_serializer = serializers.InvoiceEntryItemSerializer(item_instance, many=True)
        return Response({'invoice': serializer.data, 'items': item_serializer.data}, status.HTTP_200_OK)


class InvoiceEntryShowDetailWholesaler(generics.GenericAPIView):
    serializer_class = serializers.InvoiceEntrySerializer
    queryset = models.InvoiceEntry.objects.all()
    lookup_field = 'wholesaler_id'

    def get(self, request: Request, *args, **kwargs):
        translate(request)
        invoice_entry = models.InvoiceEntry.objects.filter(wholesaler_id_id=self.kwargs['wholesaler_id'])
        serializer = self.serializer_class(invoice_entry, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
