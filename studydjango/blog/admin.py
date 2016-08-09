from django.contrib import admin
from .models import Post, Comment

# Register your models here.
admin.site.register(Post)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'message', 'pk']
admin.site.register(Comment, CommentAdmin)