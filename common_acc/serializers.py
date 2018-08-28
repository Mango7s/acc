from rest_framework import serializers
from common_acc import models as acc_models


class AccountSerializer(serializers.ModelSerializer):
    server_name = serializers.SerializerMethodField()

    def get_server_name(self, obj):
        if obj.server:
            return obj.server.name

    class Meta:
        model = acc_models.Account
        fields = ('nikename','acc_number','acc_password','owner','server','server_name')


class ServerSerrializer(serializers.ModelSerializer):
    class Meta:
        model = acc_models.Server
        fields = '__all__'
