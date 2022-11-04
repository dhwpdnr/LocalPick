from rest_framework import generics
from .models import User
from .serializers import SignupSerializer, LoginSerializer, UserSerializer
from django.contrib.auth import login
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Signup API


class SignupAPI(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        return instance

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)

        return Response(status=status.HTTP_201_CREATED, data={"user_id": instance.id})


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        # token, created = Token.objects.get_or_create(user=user)

        # 세션에 저장(임시)
        request.session["phone_number"] = user.phone_number
        request.session["nickname"] = user.nickname
        request.session["_auth_user_id"] = user.id

        return Response({"phone": request.session["phone_number"]}, status=status.HTTP_200_OK)


class UserInfoAPI(generics.ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, pk):
        store = User.objects.get(id=pk)
        serializer = self.get_serializer(store)
        return Response(serializer.data)
