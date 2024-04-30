from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'unit', 'quantity', 'price', 'created_at', 'updated_at']


@admin.register(ProductInput)
class ProductInputAdmin(admin.ModelAdmin):
    list_display = ['product', 'description', 'created_at', 'responsible_user_id']


@admin.register(ProductOutput)
class ProductOutputAdmin(admin.ModelAdmin):
    list_display = ['product', 'description', 'removed_at', 'responsible_user_id']


class CustomUserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'position', 'tel_number',
                    'created_at', 'is_staff')  # Specify the fields to display in the admin interface


# Register the custom User model and the custom admin class
admin.site.register(User, CustomUserAdmin)

