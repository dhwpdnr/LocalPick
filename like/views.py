from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .utils import user_session_authticate

# Create your views here.


class StoreLikeListView(APIView):
    def get(self, request):
        info = user_session_authticate(request)
        if info is None:
            return redirect("users:login")
        # {{ user.정보 }}로 사용 ex) {{ user.nickname }}
        return render(request, "store/likelist.html", info)