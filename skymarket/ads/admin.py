from django.contrib import admin

from .models import Ad, Comment


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'price', 'author')
    list_filter = ('author',)
    search_fields = ('title', 'description')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'ad', 'author')
    list_filter = ('author',)
