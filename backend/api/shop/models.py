from django.db import models


# Create your models here.
class GoodsInfo(models.Model):
    id = models.AutoField(verbose_name="商品ID", primary_key=True, help_text="商品ID")
    category_choices = ((1, "宠物食品"), (2, "宠物药品"), (3, "宠物玩具"))
    category = models.IntegerField(verbose_name="商品分类", choices=category_choices, help_text="商品分类")
    title = models.CharField(verbose_name="商品标题", max_length=255, help_text="商品标题")
    image_url = models.ImageField(verbose_name="商品封面url", null=True, blank=True,
                                  upload_to='image/shop',max_length=200, help_text="商品封面url")
    text = models.TextField(verbose_name="商品介绍", help_text="商品介绍")
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True, help_text="创建时间")
    modify_time = models.DateTimeField(verbose_name="修改时间", auto_now=True, help_text="修改时间")
    price = models.DecimalField(verbose_name="售价", max_digits=10, decimal_places=2, help_text="售价")
    sold_num = models.PositiveIntegerField(verbose_name="销量", default=0, help_text="销量")
    click_num = models.IntegerField(default=0, verbose_name="点击数", help_text="点击数")
    comment_count = models.PositiveIntegerField(verbose_name="评论数", default=0, help_text="评论数")
    favor_count = models.PositiveIntegerField(verbose_name="赞数", default=0, help_text="赞数")

    class Meta:
        verbose_name = '商品信息'
        verbose_name_plural = verbose_name
        db_table = 'goods_info'

    def __str__(self):
        return self.title


class GoodsComment(models.Model):
    """
    评论表
    """
    good = models.ForeignKey(verbose_name="商品", to="GoodsInfo", on_delete=models.CASCADE, help_text="商品")
    user = models.ForeignKey(verbose_name="用户", to="users.UserInfo", on_delete=models.CASCADE, help_text="用户")

    content = models.CharField(verbose_name="评论内容", max_length=300, help_text="评论内容")
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True, help_text="创建时间")
    modify_time = models.DateTimeField(verbose_name="修改时间", auto_now=True, help_text="修改时间")

    class Meta:
        verbose_name = '商品评论'
        verbose_name_plural = verbose_name
        db_table = 'goods_comment'

    def __str__(self):
        return self.good
