from rest_framework import generics, status
from rest_framework.response import Response
from .models import Store, Image
from .serializers import StoreSerializer, ImageSerializer
from like.models import Like
from rest_framework.pagination import PageNumberPagination
from collections import OrderedDict
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class StoreCreateAPI(generics.CreateAPIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)

        return Response(status=status.HTTP_201_CREATED)


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
    page_size = 8

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
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    # 이부분(queryset) 수정 해서 보내는 쿼리 변경 / 값 안 받아도 될 때는 이렇게
    # queryset = Store.objects.all()

    serializer_class = StoreSerializer

    # pagination 설정 클래스 지정
    pagination_class = StoreListPagination

    def get_queryset(self, pk):
        # instance 는 우리가 사용할 쿼리 / url 에서 값 받아서 조회도 가능
        instance = Store.objects.filter(category_id=pk).order_by('?')
        return instance

    def get(self, request, pk, *args, **kwargs):
        # self.get_queryset() 부분은 사전에 정의 해둔 queryset 가져온
        queryset = self.filter_queryset(self.get_queryset(pk))
        user_id = request.session.get("_auth_user_id")
        store_list = queryset.values()
        for store in store_list :
            store_id = store.get("id")
            
            
            
            if Image.objects.filter(store_id=store_id).first():
                image = Image.objects.filter(store_id=store_id).first()
                
                store['image_tag'] = image.image_tag
            like = Like.objects.filter(
                user_id=user_id, store_id=store_id).first()
            if like is None:
                store['is_liked'] = False
            else :
                store['is_liked'] = True

        page = self.paginate_queryset(store_list)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(store_list)

        serializer = self.get_serializer(store_list, many=True)

        return Response(serializer.data)


class StoreImageAPI(generics.ListAPIView):
    serializer_class = ImageSerializer

    def get_queryset(self, pk):
        # instance 는 우리가 사용할 쿼리 / url 에서 값 받아서 조회도 가능
        instance = Image.objects.filter(store_id=pk)
        return instance

    def list(self, request, pk, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset(pk))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class StorePersonalListPagination(PageNumberPagination):
    page_size = 8

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


class StorePersonalListAPI(generics.ListAPIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    # 이부분(queryset) 수정 해서 보내는 쿼리 변경 / 값 안 받아도 될 때는 이렇게
    # queryset = Store.objects.all()

    serializer_class = StoreSerializer

    # pagination 설정 클래스 지정
    pagination_class = StoreListPagination

    def get_queryset(self, last_like_category):
        instance = Store.objects.filter(category_id = last_like_category)
        return instance

    def get(self, request, *args, **kwargs):
        # self.get_queryset() 부분은 사전에 정의 해둔 queryset 가져온
        user_id = request.session.get("_auth_user_id")
        like = Like.objects.filter(user_id=user_id)
        recent_like = like.order_by('id').last()
        if recent_like is None:
            stores = Store.objects.order_by("?")
            store_list = stores.values()
        else:
            last_like_category = recent_like.store_id.category_id
            queryset = self.filter_queryset(self.get_queryset(last_like_category))
            store_list = queryset.values()

        for store in store_list :
            store_id = store.get("id")
            if Image.objects.filter(store_id=store_id).first():
                image = Image.objects.filter(store_id=store_id).first()
                
                store['image_tag'] = image.image_tag
            like = Like.objects.filter(
                user_id=user_id, store_id=store_id).first()
            if like is None:
                store['is_liked'] = False
            else :
                store['is_liked'] = True

        page = self.paginate_queryset(store_list)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(store_list)

        serializer = self.get_serializer(store_list, many=True)

        return Response(serializer.data)