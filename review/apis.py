from rest_framework import generics
from rest_framework.response import Response
from .models import Review
from .serializers import ReviewSerializer
from django.shortcuts import render


class ReviewCreateAPI(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    # def get(self, request, pk):
    #     review = Review.objects.get(id=pk)
    #     serializer = self.get_serializer(review)
    #     return Response(serializer.data)


class ReviewListAPI(generics.ListAPIView):
        serializer_class = ReviewSerializer
        model = serializer_class.Meta.model

        def get_queryset(self):
            store_id = self.kwargs['pk']
            queryset = self.model.objects.filter(store_id=store_id)
            return queryset.order_by('created')
