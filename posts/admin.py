from django.contrib import admin
from .models import Post
from rest_framework.authtoken.models import Token


class AdminPosts(admin.ModelAdmin):
    list_display = ['title', 'user', 'date']
    readonly_fields = ('date',)

admin.site.register(Post, AdminPosts)
# admin.site.register(Token)
