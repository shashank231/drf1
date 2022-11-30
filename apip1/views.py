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
import coreapi
import json

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

    #     request.data.update( {'title': 'string', 'rating': 869, 'writer': 1} )
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)


class W1View(generics.RetrieveAPIView):
    serializer_class = WorkSerializer

    def get_object(self):
        id = self.kwargs.get('pk')
        w1 = Worker.objects.get(id=id)

        print("=============================")
        print(w1.boss.name)
        print(w1.boss.age)
        print(w1.boss.favemp)
        print(w1.boss.favemp.name)   # works
        print("=============================")

        return w1


class W2View(generics.ListAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkSerializer

    def get(self, request, *args, **kwargs):
        print("-----------------------------------")
        cl1 = coreapi.Client()
        s1 = cl1.get('http://127.0.0.1:8000/apip/Worker/1')
        print(type(s1))
        print(s1['name'])
        d1 = json.dumps(s1)
        print(d1)
        print(type(d1))
        # print(d1.name)
        print("------------------------------------")
        return self.list(request, *args, **kwargs)




