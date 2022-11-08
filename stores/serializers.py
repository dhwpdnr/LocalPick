from rest_framework import serializers
from .models import Store, Image


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = "__all__"
        # fields = ("title", "descriptions") 튜플로 사용
        # fields = ("title",) 튜플 하나만 사용
        # fields = ["title"] 리스트


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"
