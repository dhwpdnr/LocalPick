from rest_framework import generics
from rest_framework.response import Response
# from .serializers import LikeSerializer
# from .models import Like
from django.db.models import Q
from django.shortcuts import render


# class LikeListAPI(generics.ListAPIView):
#     serializer_class = LikeSerializer
#     def get_queryset(self, request):
#         user_id = request.session.get('_auth_user_id')
#         return Like.objects.filter(Q(user_id=user_id) & Q(is_liked=True))
#

    # class userSearch(generics.ListAPIView):
    #     serializer_class = UserSerializer
    #     filter_backends = (DjangoFilterBackend, SearchFilter)
    #     filter_fields = ('username', 'userid')
    #     search_fields = ('username', 'first_name')
    #
    #     def get_queryset(self):
    #         username = self.kwargs['username']
    #         professor = User.objects.get(username=username)
    #
    #         # Here you can do the following thing:
    #         current_user = self.request.user
    #
    #         # And use it as you wish in the filtering below:
    #
    #         return UserProfile.objects.filter(professor=professor).order_by('username')