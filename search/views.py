from django.shortcuts import render, redirect
from rest_framework.views import APIView
from stores.models import Store
from django.db.models import Q
from .utils import user_session_authticate

# Create your views here.


class SearchView(APIView):

    def get(self, request):
        info = user_session_authticate(request)
        if info is None:
            return redirect("users:login")
        return render(request, "search/search.html", info)


class SearchResultView(APIView):
    def get(self, request):
        store_list = Store.objects.all()
        search = request.GET.get('search', '')
        if search:
            search_list = store_list.filter(
                Q(store_name__icontains=search) |  # 이름
                Q(store_adress__icontains=search)  # 주소
            )

        print(search)
        print()
        print(search_list)

        return render(request, 'search.html', {'search_list': search_list, 'search': search})