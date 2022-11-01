from django.db.models import Q
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Like
from .serializers import LikeSerializer


class AppetiteCreateAPI(generics.CreateAPIView):
    serializer_class = LikeSerializer

    def post(self, request, *args, **kwargs):
        check_like = Like.objects.filter(
            user_id=request.data['user_id'], store_id=request.data['store_id']).first()
        print(check_like)
        if check_like is None:
            return self.create(request, *args, **kwargs)

        return Response(status=status.HTTP_201_CREATED)

    # TODO 좋아요 여부 확인후 칼럼 삭제 구현