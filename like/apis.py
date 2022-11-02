from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from collections import OrderedDict

from .models import Like
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
    page_size = 4

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


class StoreListAPI(generics.ListAPIView):
    # 토큰 인증 부분
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    serializer_class = LikeSerializer

    # pagination 설정 클래스 지정
    pagination_class = LikeListPagination

    def get(self, request, *args, **kwargs):
        # 가져온 user_id
        user_id = request.session.get
        # 좋아요 목록 조회 orm
        queryset = Like.objects.filter(user_id=user_id)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
