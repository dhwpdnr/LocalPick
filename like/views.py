from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .utils import user_session_authticate
from .models import Like
from users.models import User
from stores.models import Store


# Create your views here.


class StoreLikeListView(APIView):
    def get(self, request):
        info = user_session_authticate(request)
        if info is None:
            return redirect("users:login")
        # {{ user.정보 }}로 사용 ex) {{ user.nickname }}
        return render(request, "store/likelist.html", info)


def likes(request):
    if request.method == 'POST':  # ajax 방식일 때 아래 코드 실행
        store_id = request.POST['store_id']  # 좋아요를 누른 게시물id (blog_id)가지고 오기
        user_id = request.session["_auth_user_id"]  # request.user : 현재 로그인한 유저
        user = User.objects.get(id=user_id)
        store = Store.objects.get(id=store_id)

        if Like.objects.filter(user_id=user, store_id=store).exists():  # 이미 좋아요를 누른 유저일 때
            delete = Like.objects.get(user_id=user, store_id=store)
            delete.delete()
            like = False
            # Like.remove(user)  # like field에 현재 유저 추가
        else:  # 좋아요를 누르지 않은 유저일 때
            like = Like(user_id=user, store_id=store)
            like.save()
            like = True
            # like field에 현재 유저 삭제
        # post.like.count() : 게시물이 받은 좋아요 수
        response_data = {
            'is_liked':like,
            'store_id':store_id
        }
        return JsonResponse(response_data, status=201)
        # return HttpResponse(status=200, data=data)
