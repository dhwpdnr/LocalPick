from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .utils import user_session_authticate
from .models import Review

# Create your views here.


class ReviewCreateView(APIView):
    def get(self, request, pk):
        info = user_session_authticate(request)
        if info is None:
            return redirect("users:login")
        user_review = Review.objects.filter(user_id=info['user'].id, store_id=pk).first()
        if user_review is None:
            return render(request, "store/review.html")
        return redirect("/store/detail/%d" %pk )

