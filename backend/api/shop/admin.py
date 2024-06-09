from django.contrib import admin
from api.shop import models


# Register your models here.
class GoodsConfigAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'sold_num', 'create_time', 'image_url')


admin.site.register(models.GoodsInfo, GoodsConfigAdmin)
admin.site.register(models.GoodsComment)
