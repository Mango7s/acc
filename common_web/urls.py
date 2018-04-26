from django.conf.urls import url
from common_web import views


urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^handerlogin/$', views.handerlogin, name='handerlogin'),
    url(r'^account_list/$', views.account_list, name='account_list')
]