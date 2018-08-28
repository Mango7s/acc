from rest_framework import viewsets
from django.core.cache import cache
from .serializers import AccountSerializer, ServerSerrializer
from .models import Account, Server
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


class BootStrapPagination(LimitOffsetPagination):
    default_limit = 100
    offset_query_param = "offset"
    limit_query_param = "limit"
    max_limit = 10


class MyPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'page_size'


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    pagination_class = MyPageNumberPagination

    def get_queryset(self):
        queryset = Account.objects.all()
        return queryset

    def perform_create(self, serializer):
        ServerSerrializer.save()



class ServerViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerrializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset
