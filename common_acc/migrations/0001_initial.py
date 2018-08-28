# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-08-21 12:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nikename', models.CharField(max_length=64, verbose_name=b'\xe6\x98\xb5\xe7\xa7\xb0')),
                ('acc_number', models.CharField(max_length=32, verbose_name=b'\xe8\xb4\xa6\xe5\x8f\xb7')),
                ('acc_password', models.CharField(max_length=64, verbose_name=b'\xe8\xb4\xa6\xe5\x8f\xb7\xe5\xaf\x86\xe7\xa0\x81')),
                ('owner', models.CharField(max_length=64, verbose_name=b'\xe6\x8b\xa5\xe6\x9c\x89\xe8\x80\x85')),
            ],
            options={
                'verbose_name': '\u6e38\u620f\u8d26\u53f7',
                'verbose_name_plural': '\u6e38\u620f\u8d26\u53f7',
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name=b'\xe5\xa4\xa7\xe5\x8c\xba')),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u5668',
                'verbose_name_plural': '\u670d\u52a1\u5668',
            },
        ),
        migrations.AddField(
            model_name='account',
            name='server',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='common_acc.Server'),
        ),
    ]
