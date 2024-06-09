from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(verbose_name='用户名', max_length=32, db_index=True, help_text='用户名')
    password = models.CharField(verbose_name='密码', max_length=128, help_text='密码')
    token = models.CharField(verbose_name="TOKEN", max_length=64, null=True, blank=True, db_index=True, help_text="用户登录token")
    user_email = models.EmailField(verbose_name='邮箱', max_length=64, help_text='邮箱')
    category_choices = ((1, "普通用户"), (2, "宠物医生"))
    category = models.IntegerField(verbose_name="分类", choices=category_choices, help_text="用户分类")

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
        db_table = 'user_info'

    def __str__(self):
        return self.username


class DoctorInfo(models.Model):
    user = models.ForeignKey(verbose_name="医生用户", to="UserInfo", on_delete=models.CASCADE, help_text="医生用户")
    certificate_image_url = models.ImageField(verbose_name="职业证书照片", null=True, blank=True,
                                              upload_to='image/doctors', max_length=200, help_text="职业证书照片")
    certificate_number = models.CharField(verbose_name="执业证书编号", max_length=32, unique=True, db_index=True,)
    real_name = models.CharField(verbose_name="真实姓名", max_length=32, help_text="真实姓名")
    ID_number = models.CharField(verbose_name="身份证号", max_length=32, help_text="身份证号")

    class Meta:
        verbose_name = '医生额外信息'
        verbose_name_plural = verbose_name
        db_table = 'doctor_info'

    def __str__(self):
        return self.real_name
