# 作   者：林枭熠
# 开发时间:2024/6/7 下午3:24
from rest_framework import serializers

from . import models


class GoodSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)
    modify_time = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)
    """
    商品序列化器
    """
    class Meta:
        model = models.GoodsInfo
        fields = ["category", "image_url", "title", "text", "price", "create_time", "modify_time",
                  "sold_num", "click_num", "favor_count", "comment_count"]
