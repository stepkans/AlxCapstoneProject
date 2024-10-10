from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
# from django_filters.rest_framework import DjangoFilterBackend
from .models import BlogPost, Category, Tag
from .serializers import BlogPostSerializer, CategorySerializer, TagSerializer

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # filterset_fields = ['category__name', 'author__username', 'published_date', 'tags__name']
    # search_fields = ['title', 'content', 'author__username']
    # ordering_fields = ['published_date', 'category__name']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

