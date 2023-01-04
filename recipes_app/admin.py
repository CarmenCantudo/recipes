from django.contrib import admin
from .models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    """
    Admin management from Admin Panel
    Modified from I think therefore I blog, Code Institute
    """
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'ingredients', 'description']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('ingredients', 'method')
    actions = ['publish_recipes']

    def publish_recipes(self, request, queryset):
        queryset.update(status='1')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Adds comment field in admin panel
    Used from I think therefore I blog, Code Institute
    """
    list_display = ('name', 'body', 'recipe', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
