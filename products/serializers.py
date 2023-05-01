from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from products.models import Product, Category


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "slug"]


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ("id", "title", "position", "parent")

    def update(self, instance, validated_data):
        parent = validated_data.get("parent")
        if instance == parent:
            raise ValidationError("Category parent id must be different")
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.parent:
            data["parent"] = instance.parent.title
        return data
