from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .utils import user_session_authticate
from .models import Appetite

# Create your views here.


class TasteCreateView(APIView):
    def get(self, request):
        info = user_session_authticate(request)
        if info is None:
            return redirect("users:login")
        user_id = request.session.get("_auth_user_id", None)
        taste = Appetite.objects.filter(user_id=user_id).first()
        if taste is None:
            return render(request, "users/taste.html", info)
        return redirect("store:list")

