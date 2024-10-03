from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("email", "first_name", "last_name", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    ordering = ("email",)
    search_fields = ("email",)
    fieldsets = (
    )   
    filter_horizontal=()


admin.site.register(CustomUser, CustomUserAdmin )
