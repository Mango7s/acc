from django.conf.urls import include, url
from common_acc import views
from rest_framework.routers import DefaultRouter

from common_web.utils import registe_router

viewsets = (
    views.AccountViewSet,
    views.ServerViewSet
)
router = registe_router(viewsets)
# router = DefaultRouter()
# router.register(r'accounts', views.AccountViewSet, base_name='account')
# router.register(r'servers', views.ServerViewSet, base_name='server')

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
