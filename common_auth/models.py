# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.


class Team(models.Model):
    name = models.CharField('战队',max_length=64)
    logo = models.ImageField(upload_to='team_logo',null=True,default=None)
    introduction = models.TextField(null=True)

    def __unicode__(self):
        return self.name



class User(AbstractUser):
    nikename = models.CharField('昵称', max_length=64, null=True, default=None)
    mobile = models.CharField('手机号', max_length=16, null=True, default=None)
    logo = models.ImageField(upload_to='user_logo', null=True, default=None)
    introduction = models.TextField('简介',null=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, default=None)

    def __unicode__(self):
        return self.username

