from django.shortcuts import render
from rest_framework.views import APIView
from .models import Category

# Create your views here.

class StoreCreateView(APIView):
    def get(self, request):
        category_list = Category.objects.all()
        return render(request, "store/create.html", {"category_list" : category_list})