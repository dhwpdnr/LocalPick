from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
        # fields = ("title", "descriptions") 튜플로 사용
        # fields = ("title",) 튜플 하나만 사용
        # fields = ["title"] 리스트


