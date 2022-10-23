from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .utils import user_session_authticate

# Create your views here.


class ReviewCreateView(APIView):
    def get(self, request):
        info = user_session_authticate(request)
        if info is None:
            return redirect("users:login")

        return render(request, "store/review.html")
