from rest_framework import generics
from rest_framework.response import Response
from .serializers import LikeSerializer
from django.shortcuts import render


class LikeListAPI(generics.ListAPIView):
    serializer_class = LikeSerializer
    model = serializer_class.Meta.model

    # def get_queryset(self):
    #     store_id = self.kwargs['pk']
    #     queryset = self.model.objects.filter(user_id=store_id)
    #     return queryset.order_by('created')


    def get(self, request, *args, **kwargs):
        print(request.session)
        return self.list(request, *args, **kwargs)
