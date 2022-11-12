from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .utils import user_session_authticate
from rest_framework.response import Response
from .models import User


# Create your views here.
class SignupView(APIView):
    def get(self, request):
        info = user_session_authticate(request)
        if info is None:
            return render(request, "users/test.html")
        return render(request, "store/list.html")


class LoginView(APIView):
    def get(self, request):
        info = user_session_authticate(request)
        if info is None:
            return render(request, "users/login.html")
        return render(request, "store/list.html")



class FindPasswordView(APIView):
    def get(self, request):
        info = user_session_authticate(request)
        if info is None:
            return render(request, "users/password.html")
        return render(request, "store/list.html")


class ChangePasswordView(APIView):
    def get(self, request):
        info = user_session_authticate(request)
        if info is None:
            return render(request, "users/passwordch.html")
        return render(request, "store/list.html")



class MypageView(APIView):
    def get(self, request):
        info = user_session_authticate(request)
        if info is None:
            return redirect("users:login")
        return render(request, "users/mypage.html", info)


class Logout(APIView):
    def get(self, request):
        request.session.flush()
        return Response('Logged out successfully')

# class Withdrawal(APIView):
#     def post(self, request):
#         user_id = request.data["user_id"]
#         user = User.objects.get(pk=user_id)
#         user.delete()
#         request.session.flush()
#         return Response(status=200)
