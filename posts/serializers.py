from rest_framework import serializers
from .models import BlogPost, Category, Tag
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

# class BlogPostSerializer(serializers.ModelSerializer):
#     author = UserSerializer(read_only=True)
#     category = CategorySerializer()
#     tags = TagSerializer(many=True)

#     class Meta:
#         model = BlogPost
#         fields = ['id', 'title', 'content', 'author', 'category', 'tags', 'published_date', 'updated_at']

class BlogPostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)  # No need to input the author; it will be set automatically
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())  # Use primary keys for tags

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'author', 'category', 'tags', 'published_date', 'updated_at']