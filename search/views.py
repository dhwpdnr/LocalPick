from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.

class SearchView(APIView):
    def get(self, request):
        return render(request, "search/search.html")
