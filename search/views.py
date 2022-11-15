from django.shortcuts import render, redirect
from rest_framework.views import APIView
from stores.models import Store
from django.db.models import Q
from .utils import user_session_authticate
from rest_framework.response import Response


# Create your views here.


class SearchView(APIView):

    def get(self, request):
        info = user_session_authticate(request)
        if info is None:
            return redirect("users:login")
        return render(request, "search/search.html", info)


class SearchResultView(APIView):
    def get(self, request, search_word):
        info = user_session_authticate(request)
        if info is None:
            return redirect("users:login")
        info['search_word']=search_word
        print(search_word)
        print(info)
        return render(request, "search/result.html", info)