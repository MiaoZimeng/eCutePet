import uuid

from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models
from .serializers import UserRegisterSerializer, DoctorRegisterSerializer, LoginSerializer


# Create your views here.


class UserRegisterView(APIView):
    """
    用户注册,["username", "user_email", "password", "confirm_password"]
    """

    @staticmethod
    def post(request):
        # 1. 获取前端传过来的数据 ["username", "user_email", "password", "confirm_password"]
        # 2. 校验数据
        ser = UserRegisterSerializer(data=request.data)
        if ser.is_valid():
            ser.validated_data.pop('confirm_password')
            ser.save(category="1")
            return Response({'msg': '注册成功！', 'code': 200, 'data': ser.data},
                            status=status.HTTP_201_CREATED)
        else:
            return Response({"code": 400, "msg": "校验失败", "detail": ser.errors},
                            )


class DoctorRegisterView(APIView):
    """
    医生注册,["username", "user_email", "password", "confirm_password", "ID_number", "real_name", "certificate_number"]
    """

    @staticmethod
    def post(request):
        # 1. 获取前端传过来的数据 ["username", "user_email", "password",
        # "confirm_password", "ID_number", "real_name", "certificate_number"]
        # 2. 校验数据

        username = request.data.get('username')
        user_email = request.data.get('user_email')
        password = request.data.get('password')
        confirm_password = request.data.get('confirm_password')

        user_data = {'username': username, 'password': password,
                     'confirm_password': confirm_password,
                     "user_email": user_email}
        user_ser = UserRegisterSerializer(data=user_data)
        if user_ser.is_valid():
            user_ser.validated_data.pop('confirm_password')
            # url暂时为空
            real_name = request.data.get('real_name')
            ID_number = request.data.get('ID_number')
            certificate_number = request.data.get('certificate_number')
            doctor_data = {'real_name': real_name, 'ID_number': ID_number,
                           'certificate_number': certificate_number}
            doctor_serializer = DoctorRegisterSerializer(data=doctor_data)
            if doctor_serializer.is_valid():
                user = user_ser.save(category="2")
                doctor_serializer.save(user=user)
                return Response({'msg': '注册成功！', 'code': 200, 'data': doctor_serializer.data},
                                status=status.HTTP_201_CREATED)
            else:
                return Response({'msg': '校验失败', 'code': 400, "detail": doctor_serializer.errors},
                                )
        else:
            return Response({'msg': '校验失败', 'code': 400., "detail": user_ser.errors},
                            )


class LoginView(APIView):
    """
    用户登录,["username", "password"]
    return token
    """

    @csrf_exempt
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'msg': "校验失败", 'code': 400, "detail": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        instance = models.UserInfo.objects.filter(**serializer.validated_data).first()
        if not instance:
            return Response({'msg': "用户名或密码错误", 'code': 400})
        token = str(uuid.uuid4())
        instance.token = token
        instance.save()
        return Response({'msg': "登录成功", 'code': 200, 'token': token},
                        status=status.HTTP_200_OK)

# jwt登录方法
# class LoginView(TokenObtainPairView):
#     serializer_class = LoginSerializer
