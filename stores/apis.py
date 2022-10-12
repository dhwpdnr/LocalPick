from rest_framework import generics
from rest_framework.response import Response
from .models import Store
from .serializers import StoreSerializer






class StoreCreateAPI(generics.CreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    def get(self, request, pk):
        store = Store.objects.get(id=pk)
        serializer = self.get_serializer(store)
        return Response(serializer.data)


class StoreDetailAPI(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    
    def get(self, request, pk):
        store = Store.objects.get(id=pk)
        serializer = self.get_serializer(store)
        return Response(serializer.data)
    
    
class StoreListAPI(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer