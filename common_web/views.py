from django.shortcuts import render, redirect

from django.contrib import auth
from django.contrib.auth import REDIRECT_FIELD_NAME ,login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse

from rest_framework import response
from rest_framework.decorators import api_view

# Create your views here.
def index(request):
    context = {
        'title': 'Hello Django',
    }
    return render(request, 'base.html', context)


def login(request):
    return render(request, 'login.html')


@api_view(['POST'])
def handerlogin(request):
    context = {}
    username = request.data.get('username')
    password = request.data.get('password')
    user = auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        context['msg_code'] = '1'
    else:
        context['error_code'] = '1'
    return response.Response(context)


@login_required(login_url='/login/')
def account_list(request):
    return render(request, 'acc_list.html')


def logout(request):
    auth.logout(request)
    return redirect(reverse('index'))


def switch_admin(request):
    return render(request, 'testadmin.html')