from django.contrib import admin
# from django_summernote.admin import SummernoteModelAdmin
from .models import Category, Post, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name', 'category_id')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'author', 'created_date', 'category', 'status')
    list_filter = ['author', 'created_date', 'category']
    search_fields = ('author', 'content')
    actions = ['approve_posts', 'disapprove_posts']

    def approve_posts(self, request, queryset):
        queryset.update(status=1)

    def disapprove_posts(self, request, queryset):
        queryset.update(status=0)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'post', 'body', 'approved')
    list_filter = ('approved', 'created_on')
    actions = ['approve_comments', 'disapprove_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

    def disapprove_comments(self, request, queryset):
        queryset.update(approved=False)
