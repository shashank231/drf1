

from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination

class MyPageNumberPagination(PageNumberPagination):
    page_size = 2

class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 100
