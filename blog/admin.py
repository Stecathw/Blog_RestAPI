from django.contrib import admin
from .models import Category, Post, Flight_Track
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'category', 'status', 'published']
    prepopulated_fields = {'slug': ('title',)}
    
class TrackAdmin(admin.ModelAdmin):
    list_display = ['date', 'distance', 'CFD_public_link']
    
admin.site.register(Post, PostAdmin)
admin.site.register(Flight_Track, TrackAdmin)
admin.site.register(Category)