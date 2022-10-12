from django.shortcuts import render
from rest_framework.views import APIView

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

class ChangePasswordView(APIView):
    def get(self, request):
        return render(request, "users/passwordch.html")