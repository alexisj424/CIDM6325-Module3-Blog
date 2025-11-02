from django.contrib import admin
from .models import Category, Tag, Post, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name", "slug")           # <-- add this
    prepopulated_fields = {"slug": ("name",)}  # keep only if Category has slug

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name", "slug")           # <-- add this
    prepopulated_fields = {"slug": ("name",)}  # keep only if Tag has slug

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "category", "created_at")
    list_filter = ("category", "tags", "author")
    search_fields = ("title", "body")
    autocomplete_fields = ("author", "category", "tags")

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "author", "created_at")
    search_fields = ("text",)
    autocomplete_fields = ("post", "author")

