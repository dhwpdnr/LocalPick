from rest_framework import generics
from rest_framework.response import Response
from .models import Appetite
from .serializers import AppetiteSerializer


class AppetiteCreateAPI(generics.CreateAPIView):
    queryset = Appetite.objects.all()
    serializer_class = AppetiteSerializer

    # def get(self, request, pk):
    #     review = Review.objects.get(id=pk)
    #     serializer = self.get_serializer(review)
    #     return Response(serializer.data)