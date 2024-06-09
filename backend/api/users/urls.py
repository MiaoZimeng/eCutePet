# 作   者：林枭熠
# 开发时间:2024/6/6 下午8:31

from django.urls import path
from . import views
urlpatterns = [
    path(r'register/user', views.UserRegisterView.as_view(), name='user-register'),
    path(r'register/doctor', views.DoctorRegisterView.as_view(), name='user-register'),
    path(r'login/', views.LoginView.as_view(), name='login')
]
