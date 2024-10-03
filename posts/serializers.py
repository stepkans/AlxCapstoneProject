from rest_framework import serializers
from .models import BlogPost, Category, Tag
from django.contrib.auth.models import User

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

class BlogPostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    category = CategorySerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'author', 'category', 'tags', 'published_date', 'updated_date']
