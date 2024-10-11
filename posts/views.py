from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, permissions, filters
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import IsAuthorOrReadOnly 
# from django_filters.rest_framework import DjangoFilterBackend
from .models import BlogPost, Category, Tag
from .serializers import BlogPostSerializer, CategorySerializer, TagSerializer


class BlogPostViewSet(viewsets.ModelViewSet):
    """
    Only authenticated users can create Posts 
    Only the author of the blogpost can update or delete it.
    All users can view posts.
    """
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

#Creating a new post
    def perform_create(self, serializer):
        
        #Set the author of the post to the currently authenticated/logged-in user
        serializer.save(author=self.request.user)

    
    #Overriding the perform_create method
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            return Response({'message': 'Post created successfully', 'post': serializer.data}, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    #Updating a post
    def perform_update(self, serializer):       
        #Set the author of the blog post be only one who can update it
        #The author field cannot be changed by the user
        post = serializer.save(author=self.get_object().author)
        return post #Updated post
    
    #Overriding the perform_update method to update
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        #Checking if the user is the author of the post
        if instance.author != self.request.user:
            return Response({'message': 'You are not authorized to update this post'}, status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            self.perform_update(serializer) #Calls the perform_update method
            return Response({'message': 'Post updated successfully', 'post': serializer.data}, status=status.HTTP_200_OK)	
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    #Overriding the perform_destroy method to delete an existing post
    #Returns a custom response
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        #Checking if the user is the author of the post
        if instance.author != self.request.user:
            return Response({'message': 'You are not authorized to delete this post'}, status=status.HTTP_403_FORBIDDEN)
        
        self.perform_destroy(instance)
        return Response({'message': 'Post deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

