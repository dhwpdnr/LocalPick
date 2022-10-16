from django.shortcuts import render
from rest_framework.views import APIView
from .models import Category, Image, Store
from users.models import User
from django.views.decorators.csrf import csrf_exempt
import os
from uuid import uuid4
from LocalPick.settings import STORE_IMAGE
from rest_framework.response import Response

# Create your views here.

class StoreCreateView(APIView):
    def get(self, request):
        category_list = Category.objects.all()
        return render(request, "store/create.html", {"category_list" : category_list})


class StoreImageCreate(APIView):
    @csrf_exempt
    def post(self, request):

        store_id = request.data.get('store_id')
        image_list = request.FILES.getlist('files')

        for i in image_list :

            uuid_name = uuid4().hex
            save_path = os.path.join(STORE_IMAGE, uuid_name)
            with open(save_path, 'wb+') as destination:
                for chunk in i.chunks():
                    destination.write(chunk)

            image = uuid_name

            Image.objects.create(image_tag=image, store_id=store_id)
        return Response(status=200)


class StoreDetailView(APIView):
    def get(self, request, pk):
        session_user_id = request.session.get('_auth_user_id')
        user_id = User.objects.filter(id = session_user_id).first()
        if user_id is None :
            return render(request, "users/login.html")

        return render(request, "store/detail.html", {"pk" : pk})


class StoreListView(APIView):
    def get(self, request):
        session_user_id = request.session.get('_auth_user_id')
        user_id = User.objects.filter(id=session_user_id).first()
        if user_id is None:
            return render(request, "users/login.html")

        store_list = Store.objects.all()
        return render(request, "store/list.html", {"store_list": store_list})