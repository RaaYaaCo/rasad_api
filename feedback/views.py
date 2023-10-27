from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .serializers import ComplaintSerializer
from .models import Complaint


class ComplaintView(generics.GenericAPIView):
    serializer_class = ComplaintSerializer
    queryset = Complaint

    def post(self, request: Request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

