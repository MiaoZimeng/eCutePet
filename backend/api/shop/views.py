from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from .models import GoodsInfo
from .serializers import GoodSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class GoodsPagination(PageNumberPagination):
    page_size = 16
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 50


class GoodViewSet(ReadOnlyModelViewSet):
    """
    获取商品列表，分页，搜索，过滤，排序
    """
    # 数据库查询集
    queryset = GoodsInfo.objects.get_queryset().order_by('id')
    # 序列化器
    serializer_class = GoodSerializer
    # 分页
    pagination_class = GoodsPagination
    # 过滤三件套
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # 过滤字段，对应DjangoFilterBackend，默认为精准匹配
    filterset_fields = ['title', 'text']
    # filter_class = GoodsFilter 自己定义的过滤类
    # 关键词搜索字段，对应SearchFilter，默认为模糊匹配
    search_fields = ['title', 'text']
    # 关键词搜索字段，对应OrderingFilter，默认为升序排序
    ordering_fields = ['title', 'price', 'sold_num', 'create_time', "favor_count", "click_num", "comment_count"]

    # 商品点击数+1
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click_num += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class GoodModifyViewSet(ModelViewSet):
    """
    对商品进行任何修改
    """
    # 认证组件
    authentication_classes = []
    # 权限组件
    permission_classes = []
    # 数据库查询集
    queryset = GoodsInfo.objects.get_queryset().order_by('id')
    # 序列化器
    serializer_class = GoodSerializer
    # 分页
    pagination_class = GoodsPagination
    # 过滤三件套
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # 过滤字段，对应DjangoFilterBackend，默认为精准匹配
    # filterset_fields = ['name', 'leader', 'id']
    # filter_class = GoodsFilter 自己定义的过滤类
    # 关键词搜索字段，对应SearchFilter，默认为模糊匹配
    search_fields = ['title', 'text']
    # 关键词搜索字段，对应OrderingFilter，默认为升序排序
    ordering_fields = ['title', 'price', 'sales_volume', 'create_time']

    # # 商品点击数+1
    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     instance.click_num += 1
    #     instance.save()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)
