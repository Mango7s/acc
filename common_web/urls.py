from django.conf.urls import url
from common_web import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^handerlogin/$', views.handerlogin, name='handerlogin'),
    url(r'^acc_list/$', views.account_list, name='acc_list')
]
