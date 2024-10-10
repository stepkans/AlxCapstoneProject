from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogPostViewSet, CategoryViewSet,TagViewSet

router = DefaultRouter()
router.register('posts', BlogPostViewSet)
router.register('categories', CategoryViewSet)
router.register('tags', TagViewSet)

urlpatterns = [
    path('', include(router.urls)),
]