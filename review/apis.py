from rest_framework import generics
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class ReviewCreateAPI(generics.CreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    # def get(self, request, pk):
    #     review = Review.objects.get(id=pk)
    #     serializer = self.get_serializer(review)
    #     return Response(serializer.data)


class ReviewListAPI(generics.ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = ReviewSerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        store_id = self.kwargs['pk']
        queryset = self.model.objects.filter(store_id=store_id)
        return queryset.order_by('created')
