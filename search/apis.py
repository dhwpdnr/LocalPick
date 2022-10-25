from stores.serializers import StoreSerializer
from rest_framework import generics
from stores.models import Store
from rest_framework.response import Response
from django.db.models import Q


class SearchAPI(generics.ListAPIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    serializer_class = StoreSerializer

    def get_queryset(self, search):
        # instance 는 우리가 사용할 쿼리 / url 에서 값 받아서 조회도 가능
        instance = Store.objects.filter(
                Q(store_name__icontains=search) |
                Q(store_adress__icontains=search))
        return instance

    def get(self, request, *args, search_word, **kwargs):
        # self.get_queryset() 부분은 사전에 정의 해둔 queryset 가져온
        queryset = self.filter_queryset(self.get_queryset(search_word))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
