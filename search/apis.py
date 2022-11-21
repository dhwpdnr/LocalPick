from stores.serializers import StoreSerializer
from rest_framework import generics
from stores.models import Store
from rest_framework.response import Response
from django.db.models import Q
from collections import OrderedDict
from rest_framework.pagination import PageNumberPagination

from stores.models import Image
from like.models import Like
from django.shortcuts import render


class SearchPagination(PageNumberPagination):
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

class SearchAPI(generics.ListAPIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = StoreSerializer

    pagination_class = SearchPagination

    def get_queryset(self, search_word):
        # instance 는 우리가 사용할 쿼리 / url 에서 값 받아서 조회도 가능
        instance = Store.objects.filter(
            Q(store_name__icontains=search_word) |
            Q(store_adress__icontains=search_word))
        return instance

    def get(self, request, search_word, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset(search_word))
        user_id = request.session.get("_auth_user_id")
        store_list = queryset.values()
        for store in store_list:
            store_id = store.get("id")
            image = Image.objects.filter(store_id=store_id).first()
            store['image_tag'] = image.image_tag
            like = Like.objects.filter(
                user_id=user_id, store_id=store_id).first()
            if like is None:
                store['is_liked'] = False
            else:
                store['is_liked'] = True

        page = self.paginate_queryset(store_list)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(store_list)

        serializer = self.get_serializer(store_list, many=True)

        return Response(serializer.data)
