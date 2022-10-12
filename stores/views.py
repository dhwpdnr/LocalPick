from django.shortcuts import render
from rest_framework.views import APIView
from .models import Category
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

class StoreCreateView(APIView):
    def get(self, request):
        category_list = Category.objects.all()
        return render(request, "store/create.html", {"category_list" : category_list})

class StoreImageCreate(APIView):
    @csrf_exempt
    def post(self, request):
        print(request.FILES)
        return render(request, "store/create.html")

    # < MultiValueDict: {'files': [ < InMemoryUploadedFile: 툴바1.png(image / png) >, < InMemoryUploadedFile: 툴바2.png(
    #     image / png) >, < InMemoryUploadedFile: Flowchart.jpg(image /) >]} >