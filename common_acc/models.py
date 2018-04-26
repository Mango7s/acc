# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class Server(models.Model):
    name = models.CharField('大区', max_length=64)

    class Meta:
        verbose_name = '服务器'
        verbose_name_plural = '服务器'

    def __unicode__(self):
        return self.name


class Account(models.Model):
    nikename = models.CharField('昵称', max_length=64)
    acc_number = models.CharField('账号', max_length=32)
    acc_password = models.CharField('账号密码', max_length=64)
    owner = models.CharField('拥有者', max_length=64)
    server = models.ForeignKey(Server, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = '游戏账号'
        verbose_name_plural = '游戏账号'

    def __unicode__(self):
        return self.nikename



