from django.contrib import admin
from app.models import Post, Comment


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
