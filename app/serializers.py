from rest_framework import serializers
from .models import Design, DesignCategory


class DesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Design
        fields = ['picture', 'category', 'created_at']


class DesignCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DesignCategory
        fields = ['id', 'name', 'description', 'image', 'created_at']


