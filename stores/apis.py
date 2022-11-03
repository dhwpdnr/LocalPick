from rest_framework import generics
from rest_framework.response import Response
from .models import Store
from .serializers import StoreSerializer
from like.models import Like
from rest_framework.pagination import PageNumberPagination
from collections import OrderedDict
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class StoreCreateAPI(generics.CreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

    def get(self, request, pk):
        store = Store.objects.get(id=pk)
        serializer = self.get_serializer(store)
        return Response(serializer.data)


class StoreDetailAPI(generics.ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    
    def get(self, request, pk):
        store = Store.objects.get(id=pk)
        serializer = self.get_serializer(store)
        store_like = Like.objects.filter(store_id=pk)
        store_data = serializer.data
        like_count = store_like.count()
        store_data['like_count'] = like_count

        return Response(store_data)

    
class StoreListPagination(PageNumberPagination):
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
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    # 이부분(queryset) 수정 해서 보내는 쿼리 변경 / 값 안 받아도 될 때는 이렇게
    # queryset = Store.objects.all()

    serializer_class = StoreSerializer

    # pagination 설정 클래스 지정
    pagination_class = StoreListPagination

    # TODO django filter /?search 확인 해보기
    # filter_backends = (DjangoFilterBackend, SearchFilter)
    # search_fields = ("category")

    def get_queryset(self, pk):
        # instance 는 우리가 사용할 쿼리 / url 에서 값 받아서 조회도 가능
        instance = Store.objects.filter(category_id=pk)
        return instance

    def get(self, request, pk, *args, **kwargs):
        # self.get_queryset() 부분은 사전에 정의 해둔 queryset 가져온
        queryset = self.filter_queryset(self.get_queryset(pk))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)





# TODO 좋아요 manytomany 확인 해보기