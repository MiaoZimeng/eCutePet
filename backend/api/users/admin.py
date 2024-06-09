from django.contrib import admin

from api.users import models


class UsersConfigAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'user_email', 'category')


class DoctorConfigAdmin(admin.ModelAdmin):
    list_display = ('real_name', 'ID_number', 'certificate_image_url')


# Register your models here.

admin.site.register(models.UserInfo, UsersConfigAdmin)
admin.site.register(models.DoctorInfo, DoctorConfigAdmin)
