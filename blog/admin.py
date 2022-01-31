from django.contrib import admin
from .models import Category, Post, Flight_Track, Photo
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'category', 'status', 'published']
    prepopulated_fields = {'slug': ('title',)}
    
class TrackAdmin(admin.ModelAdmin):
    list_display = ['id','date', 'distance', 'category', 'CFD_public_link']
    
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'status', 'slug', 'author']
    prepopulated_fields = {'slug': ('title',),}
    
    
admin.site.register(Post, PostAdmin)
admin.site.register(Flight_Track, TrackAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Category)