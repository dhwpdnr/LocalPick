from stores.serializers import StoreSerializer
from rest_framework import generics
from stores.models import Store
from rest_framework.response import Response
from django.db.models import Q
from django.shortcuts import render


class SearchAPI(generics.ListAPIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = StoreSerializer

    def get_queryset(self):
        # instance 는 우리가 사용할 쿼리 / url 에서 값 받아서 조회도 가능
        instance = Store.objects.all()
        return instance

    def get(self, request, search_word, *args, **kwargs):
        print(search_word)
        query = self.filter_queryset(self.get_queryset())
        queryset = query.filter(
            Q(store_name__icontains=search_word) |
            Q(store_adress__icontains=search_word))
        serializer = self.get_serializer(queryset, many=True)
        print(serializer.data)
        return Response(serializer.data)
