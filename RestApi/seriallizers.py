from rest_framework import serializers
from .models import Blog

class BlogSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = Blog

        fields = [
            'pk',
            'title',
            'desc'
        ]

        read_only_fields = [
            'pk'
        ]