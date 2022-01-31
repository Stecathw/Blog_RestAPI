# DRF Modelviewset
from rest_framework import viewsets
# Model
from blog.models import Photo, Flight_Track, Post
# Serializer
from .serializers import PhotoListSerializer, PostSerializer, PostListSerializer, FlightTrackListSerializer
# Single object
from django.shortcuts import get_object_or_404


class PostViewSet(viewsets.ModelViewSet):
    """
    A ModelViewSet for listing posts and retrieving single post. 
    Deleting and updating posts is only possible for admin. (Permissions under settings.py)
    NB : Inherits from GenericAPIView (attributes and methods) and provide all type of mixins actions.
    """      
    
    # We use for now 2 serializers :  
    serializer_classes = {
            'list': PostListSerializer,
            'retrieve': PostSerializer,
        }
    # Specifying default one
    default_serializer_class = PostSerializer 
    
    def get_queryset(self):
        """
        Returns the queryset that should be used for list views,
        used as the base for lookups in detail views.
        """        
        return Post.publicpostobjects.all()
    
    def get_object(self, queryset=None, **kwargs):
        """
        Returns an object instance that should be used for detail views.
        """
        item = self.kwargs.get('pk')
        obj = get_object_or_404(Post, slug=item)
        return obj

    def get_serializer_class(self):
        """
        Returns according serializer
        Both DRF actions "List" and "Retrieve" are both GET requests.
        """
        return self.serializer_classes.get(self.action, self.default_serializer_class)


class FlightTrackViewSet(viewsets.ModelViewSet):
    
    serializer_class = FlightTrackListSerializer
    default_serializer_class = PostSerializer

    def get_queryset(self):
        """
        Returns the queryset that should be used for list views,
        used as the base for lookups in detail views.
        """        
        return Flight_Track.objects.all()
    
    
class PhotoViewSet(viewsets.ModelViewSet):
    
    serializer_class = PhotoListSerializer
    
    def get_queryset(self):
        return Photo.publicphotosobjects.all()