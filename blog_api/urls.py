# from django.urls import path
from .views import PhotoViewSet, FlightTrackViewSet, PostViewSet

from rest_framework.routers import DefaultRouter

app_name = 'blog_api'

router = DefaultRouter()

router.register(r'posts', PostViewSet, basename='post')
router.register(r'tracks', FlightTrackViewSet, basename='track')
router.register(r'photos', PhotoViewSet, basename='photos')
urlpatterns = router.urls

# urlpatterns=[
#     path('', PostList.as_view(), name='list_create'),
#     path('<int:pk>', PostList.as_view(), name='detail_create'),
# ]
