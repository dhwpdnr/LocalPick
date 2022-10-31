from rest_framework import generics
from rest_framework.response import Response
from .models import Like
from .serializers import LikeSerializer


class AppetiteCreateAPI(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    # TODO 좋아요 여부 확인후 테이블 추가 혹은 삭제