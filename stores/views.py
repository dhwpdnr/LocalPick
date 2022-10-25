from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .models import Category, Image, Store
from users.models import User
from django.views.decorators.csrf import csrf_exempt
import os
from uuid import uuid4
from LocalPick.settings import STORE_IMAGE
from rest_framework.response import Response
from .utils import user_session_authticate


# Create your views here.

class StoreCreateView(APIView):
    def get(self, request):
        category_list = Category.objects.all()
        return render(request, "store/create.html", {"category_list": category_list})


class StoreImageCreate(APIView):
    @csrf_exempt
    def post(self, request):

        store_id = request.data.get('store_id')
        image_list = request.FILES.getlist('files')

        for i in image_list:

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
        info = user_session_authticate(request)
        if info is None:
            return redirect("users:login")
        # info에 url 에서 받아온 pk 담아서 넘김
        info['pk'] = pk

        return render(request, "store/detail.html", info)


class StoreListView(APIView):
    def get(self, request):
        info = user_session_authticate(request)
        if info is None:
            return redirect("users:login")
        # {{ user.정보 }}로 사용 ex) {{ user.nickname }}
        return render(request, "store/list.html", info)


class StoreLikeListView(APIView):
    def get(self, request):
        info = user_session_authticate(request)
        if info is None:
            return redirect("users:login")
        # {{ user.정보 }}로 사용 ex) {{ user.nickname }}
        return render(request, "store/likelist.html", info)


class Test(APIView):
    def get(self, request):
        info = user_session_authticate(request)
        if info is None:
            return redirect("users:login")
        # {{ user.정보 }}로 사용 ex) {{ user.nickname }}
        return render(request, "store/test.html", info)


class StoreLike(APIView):
    def post(self, request):
        print(request.POST)
        # pk = request.get('pk', None)
        # user_id = request.session.get("_auth_user_id", None)

        # if Store.like_users.filter(id=user_id).exists():
        #     Store.like_users.remove()
        #     message = "좋아요 취소"
        # else:
        #     Store.like_users.add()
        #     message = "좋아요"

        # context = {'likes_count' : Store.count_like_users()}
        return Response(status=200)


    # def video_like(request):
    #     pk = request.POST.get('pk', None)
    #     video = get_object_or_404(Video, pk=pk)
    #     user = request.user
    #
    #     if video.likes_user.filter(id=user.id).exists():
    #         video.likes_user.remove(user)
    #         message = '좋아요 취소'
    #     else:
    #         video.likes_user.add(user)
    #         message = '좋아요'
    #
    #     context = {'likes_count': video.count_likes_user(), 'message': message}
    #     return HttpResponse(json.dumps(context), content_type="application/json")
    #TODO MANYTOMANY 확인
