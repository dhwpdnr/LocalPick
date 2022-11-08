from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from stores.models import Store, Image

# Create your views here.


class StoreUpload(APIView):
    def post(self, request):
        store_list = request.data
        for store in store_list:
            store_name = store["store_name"]
            store_tel = store["store_tel"]
            store_adress = store["store_adress"]
            category_id = store["category"]
            store_images = store["imgs"]
            store_data = Store.objects.create(store_name=store_name, store_tel=store_tel, store_adress=store_adress, category_id=category_id)
            for imgs in store_images:
                image = Image.objects.create(store_id=store_data.id, image_tag=imgs)
        return Response(status=200)
