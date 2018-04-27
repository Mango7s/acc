from django.conf.urls import include, url
from common_acc import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'accounts', views.AccountViewSet, base_name='account')
router.register(r'server', views.ServerViewSet, base_name='server')

urlpatterns = [
    url(r'', include(router.urls)),
]
