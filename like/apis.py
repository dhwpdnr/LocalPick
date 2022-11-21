from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from collections import OrderedDict

from .models import Like
from stores.models import Image, Store
from .serializers import LikeSerializer


class LikeAPI(generics.CreateAPIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = LikeSerializer

    def post(self, request, *args, **kwargs):

        check_like = Like.objects.filter(
            user_id=request.data['user_id'], store_id=request.data['store_id']).first()
        print(check_like)
        if check_like is None:
            return self.create(request, *args, **kwargs)
        delete = Like.objects.get(user_id=request.data['user_id'], store_id=request.data['store_id'])
        delete.delete()
        return Response(status=200)


class LikeListPagination(PageNumberPagination):
    page_size = 10

    def get_paginated_response(self, data):
        try:
            previous_page_number = self.page.previous_page_number()
        except:
            previous_page_number = None

        try:
            next_page_number = self.page.next_page_number()
        except:
            next_page_number = None

        return Response(
            OrderedDict(
                [
                    ("storeList", data),
                    ("pageCnt", self.page.paginator.num_pages),
                    ("curPage", self.page.number),
                    ("nextPage", next_page_number),
                    ("previousPage", previous_page_number),
                ]
            )
        )


class LikeListAPI(generics.ListAPIView):
    # 토큰 인증 부분
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    serializer_class = LikeSerializer

    # pagination 설정 클래스 지정
    pagination_class = LikeListPagination

    def get_queryset(self,user_id):
        instance = Like.objects.filter(user_id=user_id)
        return instance

    def get(self, request, *args, **kwargs):
        # 가져온 user_id
        user_id = request.session.get("_auth_user_id")
        # 좋아요 목록 조회 orm
        queryset = self.filter_queryset(self.get_queryset(user_id))
        like_list = queryset.values()
        for store in like_list :
            store_id = store.get("store_id_id")
            image = Image.objects.filter(store_id=store_id).first()
            store['image_tag'] = image.image_tag
            stores = Store.objects.get(id=store_id)
            store['store_name'] = stores.store_name
            like = Like.objects.filter(
                user_id=user_id, store_id=store_id).first()
            if like is None:
                store['is_liked'] = False
            else :
                store['is_liked'] = True
        page = self.paginate_queryset(like_list)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(like_list)

        serializer = self.get_serializer(like_list, many=True)
        return Response(serializer.data)

        # store 정보 사용 할때 "data.store_id.원하는 정보 " 이런식으로 사용