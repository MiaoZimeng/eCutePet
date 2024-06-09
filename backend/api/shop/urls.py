# 作   者：林枭熠
# 开发时间:2024/6/7 上午11:45

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'user/goods', views.GoodViewSet, basename='user-goods')
# router.register(r'admin/goods', views.GoodModifyViewSet, basename='admin-goods')

urlpatterns = [
    path('', include(router.urls)),
    # 添加其他非ViewSet的API视图

]
