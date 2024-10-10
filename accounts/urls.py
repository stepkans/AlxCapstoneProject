from django.urls import path, include
from .import views


urlpatterns = [
    path('register/', views.registerUser, name='registerUser'),
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate')
]