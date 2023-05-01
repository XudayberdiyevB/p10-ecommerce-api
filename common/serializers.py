from rest_framework import serializers

from common.models import Category


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ("id", "title", "position", "parent")
