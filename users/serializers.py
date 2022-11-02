from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate, login
from rest_framework import serializers, status
from rest_framework.validators import UniqueValidator
from rest_framework.response import Response

from rest_framework.authtoken.models import Token
from .models import User


class SignupSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
    )
    password2 = serializers.CharField(write_only=True, required=True)
    birth = serializers.DateField()
    gender = serializers.CharField()
    nickname = serializers.CharField(validators = [UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField()

    class Meta:
        model = User
        fields = ("username", "phone_number", "password", "password2", "birth", "gender", "nickname")

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        return data

    def create(self, validated_data):
        # username = validated_data["username"]
        # phone_number = validated_data["phone_number"]
        # user = User.objects.create_user(phone_number)
        # user.username = username
        # user.set_password(validated_data["password"])
        # user.save()
        
        user = User.objects.create(
        	phone_number = validated_data['phone_number'],
            username = validated_data['username'],
            nickname = validated_data['nickname'],
            gender = validated_data['gender'],
            birth = validated_data['birth']
        )
        user.set_password(validated_data["password"])
        
        user.save()
        user_id = user.id
        token = Token.objects.create(user=user)
        # token_return = Token.Token.objects.filter(user=user).first()
        #
        # return Response({"token": token_return.key}, status=200)
        # return Response({"user_id":user_id}, status=200)
        return user

class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user:
            # token = Token.objects.get(user=user)
            # return token
            data["user"] = user
            return data
        raise serializers.ValidationError(
            {"error": "Unable to log in with provided credentials."}
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("nickname", "phone_number", "gender", "username")
        # fields = ("title",) 튜플 하나만 사용
        # fields = ["title"] 리스트