from rest_framework import generics
from rest_framework.response import Response

from .serializers import ReviewSerializer

from users.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class ReviewCreateAPI(generics.CreateAPIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = ReviewSerializer


class ReviewListAPI(generics.ListAPIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = ReviewSerializer
    model = serializer_class.Meta.model

    def get_queryset(self, pk):
        # instance 는 우리가 사용할 쿼리 / url 에서 값 받아서 조회도 가능
        instance = self.model.objects.filter(store_id=pk)
        return instance.order_by('created')

    def get(self, request, pk, *args, **kwargs):
        # self.get_queryset() 부분은 사전에 정의 해둔 queryset 가져온
        queryset = self.filter_queryset(self.get_queryset(pk))
        review_list = queryset.values()
        print(review_list)
        for review in review_list:
            user_id = review.get("user_id_id")
            print(user_id)
            user = User.objects.filter(id=user_id).first()
            print(user.nickname)
            review['nickname'] = user.nickname


        return Response(review_list)
