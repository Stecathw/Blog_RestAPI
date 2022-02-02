from rest_framework import serializers
from blog.models import Photo, Post, Flight_Track


class PostSerializer(serializers.ModelSerializer):
    """
    Returns all infos about a post : send whole data to details view.
    """
    class Meta:
        model = Post
        fields = '__all__'

        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
        
class PostListSerializer(serializers.ModelSerializer):
    """
    Returns only general info about a post : avoid sending whole content to list view.
    """
    
    category = serializers.StringRelatedField()
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'published', 'sum_up', 'slug', 'category']
        

class FlightTrackListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Flight_Track
        fields = '__all__'
        
class PhotoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'