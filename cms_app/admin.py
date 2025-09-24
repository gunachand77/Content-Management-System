from django.contrib import admin
from .models import Category, Page

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'created_at', 'is_published']