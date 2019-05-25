from rest_framework import serializers
from .models import Post


class CustomUserSerializer(serializers.Serializer):
    full_name = serializers.SerializerMethodField()
    email = serializers.EmailField()
    username = serializers.CharField()

    @staticmethod
    def get_full_name(obj):
        return obj.get_full_name()

    # @staticmethod
    # def get_email(obj):
    #     return obj.email


class PostSerializer(serializers.ModelSerializer):
    # author = serializers.ReadOnlyField(source='user.id')
    author = CustomUserSerializer(source='user', read_only=True)

    class Meta:
        model = Post
        fields = 'title', 'author', 'date'
