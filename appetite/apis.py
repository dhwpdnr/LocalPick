from rest_framework import generics
from rest_framework.response import Response
from .models import Appetite
from .serializers import AppetiteSerializer


class AppetiteCreateAPI(generics.CreateAPIView):
    queryset = Appetite.objects.all()
    serializer_class = AppetiteSerializer
