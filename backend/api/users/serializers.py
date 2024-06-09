# 作   者：林枭熠
# 开发时间:2024/6/6 下午10:30

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from rest_framework import serializers

from ext.hook import HookSerializer
from .models import UserInfo, DoctorInfo


class UserRegisterSerializer(HookSerializer, serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = UserInfo
        fields = ["id", "username", "user_email", "password", "confirm_password", "category"]
        extra_kwargs = {
            "id": {"read_only": True},
            "password": {"write_only": True},
            "category": {"read_only": True}
        }

    def validate_username(self, value):
        if UserInfo.objects.filter(username=value).exists():
            raise serializers.ValidationError("用户名已被注册！")
        return value
    
    def validate_user_email(self, value):
        if UserInfo.objects.filter(user_email=value).exists():
            raise serializers.ValidationError("邮箱已被注册！")
        return value

    def validate_confirm_password(self, value):
        password = self.initial_data.get("password")
        if password != value:
            raise serializers.ValidationError("两次密码输入不一致！")
        return value

    @staticmethod
    def nb_category(obj):
        return obj.get_category_display()


class DoctorRegisterSerializer(serializers.ModelSerializer):
    user = UserRegisterSerializer(read_only=True)

    class Meta:
        model = DoctorInfo
        fields = ["user", "ID_number", "real_name", "certificate_number"]

    def validate_ID_number(self, value):
        if DoctorInfo.objects.filter(ID_number=value).exists():
            raise serializers.ValidationError("该身份证号已被注册。")
        return value

    def validate_certificate_number(self, value):
        if DoctorInfo.objects.filter(certificate_number=value).exists():
            raise serializers.ValidationError("该执业证号已被注册。")
        return value



class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ["username", "password"]
        extra_kwargs = {
            "id": {"read_only": True},
        }

# class LoginSerializer(TokenObtainPairSerializer):
#     class Meta:
#         model = UserInfo
#         fields = ["username", "password"]
#         extra_kwargs = {
#             "id": {"read_only": True},
#         }
