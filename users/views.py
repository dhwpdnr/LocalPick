from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .utils import user_session_authticate


# Create your views here.
class SignupView(APIView):
    def get(self, request):
        return render(request, "users/signup.html")


class LoginView(APIView):
    def get(self, request):
        return render(request, "users/login.html")


class FindPasswordView(APIView):
    def get(self,request):
        return render(request, "users/password.html")


class TestView(APIView):
    def get(self, request):
        return render(request, "users/test.html")


class ChangePasswordView(APIView):
    def get(self, request):
        return render(request, "users/passwordch.html")


class MypageView(APIView):
    def get(self, request):
        info = user_session_authticate(request)
        if info is None:
            return redirect("users:login")
        return render(request, "users/mypage.html", info)