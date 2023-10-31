# monti 123
# request.data._mutable = True
# serializer.validated_data
# serializer.data
# request.data
# from annoying.functions import get_object_or_None

from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from drf_yasg.utils import swagger_auto_schema
from .mypagination import MyPageNumberPagination, MyLimitOffsetPagination

from django.core.cache import cache
from django.db.models import Case, Value, When
from .models import *

from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from pprint import pprint
from rest_framework.permissions import BasePermission

class IsBookOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user is the owner of the book
        # return obj.owner == request.user
        # if obj.name == 'a1':
        #     return False
        return False

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

class AuthorView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    # authentication_classes = [ BasicAuthentication ]
    # permission_classes = [ IsAuthenticated, IsBookOwner ]

    # def get_object(self):
    #     id1 = self.kwargs.get('pk')
    #     print("id1 = ", id1)
    #     return Author.objects.get(id=id1)

    # def retrieve(self, request, *args, **kwargs):
    #     print(" - - - - - - - - - - - - - - - - - - ")
    #     instance = self.get_object()
    #     self.check_object_permissions(request, instance)
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)


class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # pagination_class = MyLimitOffsetPagination

    # def list(self, request, *args, **kwargs):
    #     dict1 = {
    #         "key1": 1,
    #         "key2": "spmething",
    #         "key3": True
    #     }

    def my_fun(self):
        b = cache.get('key1', 'non')
        if b == "non":
            a = Point(1, 2)
            b = cache.set('key1', a, 15)
            b = cache.get('key1')
            print("@@@")
            print(b)
            return b


    def list(self, request, *args, **kwargs):
        queryset = Book.objects.all()
        b_ser = BookSerializer(queryset, many=True)
        a11 = Response(b_ser.data)
        val1 = self.my_fun()
        print("namo")
        return a11


    def create(self, request, *args, **kwargs):
        print(" - - - aya - - - ")
        print(dict(request.data))
        print("without id = ", request.data.get('writer'))
        print(request.data.get('writer_id'))
        print("- 9--")
        b1 = Book.objects.filter(rating=12)
        print('b1 = ', b1)
        b1.update(
            rating=13
        )
        print("farzi-1")



        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    #     return Response(dict1)

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

    def list(self, request, *args, **kwargs):

        lst1 = Worker.objects.annotate(
            is_coder=Case(
            When(in_dept="Code", then=Value("Yes")),
            default=Value("No"),
            )
        ).values_list("name", "is_coder")

        print(lst1)

        return super(W2View, self).list(request, *args, **kwargs)


class EmployeeRetrieve(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    d1 = dict(Employee._meta.get_field('salary_class').choices)

    def get(self, request, *args, **kwargs):
        # d1 = dict(Employee.SALARY_CLASS_CHOICES)
        print(self.d1)
        return super(EmployeeRetrieve, self).get(request, *args, **kwargs)





