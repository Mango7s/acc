from rest_framework import viewsets
from django.core.cache import cache
from .serializers import AccountSerializer, ServerSerrializer
from .models import Account, Server


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

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