from django.contrib import admin
from .models import Account, Server

# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display = ('nikename', 'acc_number', 'acc_password', 'owner', 'server')

class ServerAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Account, AccountAdmin)
admin.site.register(Server, ServerAdmin)
