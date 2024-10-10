from django.db import models
from django.conf import settings
# Create your models here.
class Category(models.Model):
    """Class representing the category of a blog post """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    """Class representing the TAG of a blog post """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name    
class BlogPost(models.Model):
    """Class representing the fields of a blog post """
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title    