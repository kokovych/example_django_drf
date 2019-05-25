from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField(source='user')

    class Meta:
        model = Post
        fields = 'title', 'author', 'date'

    def get_author(self, obj):
        return obj.user.id
