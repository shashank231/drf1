# monti 123
# request.data._mutable = True
# serializer.validated_data
# serializer.data
# request.data

from . models import *
from .serializers import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from drf_yasg.utils import swagger_auto_schema
from .mypagination import MyPageNumberPagination, MyLimitOffsetPagination

import pdb

class AuthorView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = MyLimitOffsetPagination

    def get(self, request, *args, **kwargs):
        print("u+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        return self.list(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     request.data._mutable = True
    #     request.data.update({"rating": 17})
    #     return super(BookView, self).post(request, *args, **kwargs)


class BookDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """
    BookView Update
    ---
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    # @swagger_auto_schema( request_body = DummySerializer )
    # def put(self, request, *args, **kwargs):
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()


    #     print("----------------------------------------------------------------------------------------------------------")
    #     print("req.data = ", request.data)
    #     print(type(request.data))
    #     b = request.data.get("section", "harharmahadev")
    #     print("b = ", b)
    #     #request.data.update({"section", "st2"})
    #     ser = DummySerializer(data=request.data)
    #     if ser.is_valid(raise_exception=True):
    #         print("ser.data = ", ser.data)
    #         print(type(ser.data))
    #         a = ser.data.get("section", "har har har")
    #         print("a = ", a)
    #     print("----------------------------------------------------------------------------------------------------------")


    #     request.data.update( {'title': 'string', 'rating': 869, 'writer': 1} )
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)


    




