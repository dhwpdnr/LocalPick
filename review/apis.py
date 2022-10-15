from rest_framework import generics
from rest_framework.response import Response
from .models import Review
from .serializers import ReviewSerializer




class StoreCreateAPI(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # def get(self, request, pk):
    #     review = Review.objects.get(id=pk)
    #     serializer = self.get_serializer(review)
    #     return Response(serializer.data)