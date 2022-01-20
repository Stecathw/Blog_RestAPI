from posixpath import basename
# from django.urls import path
from .views import PostViewSet

from rest_framework.routers import SimpleRouter

app_name = 'blog_api'

router = SimpleRouter()

router.register(r'', PostViewSet, basename='post')
urlpatterns = router.urls

# urlpatterns=[
#     path('', PostList.as_view(), name='list_create'),
#     path('<int:pk>', PostList.as_view(), name='detail_create'),
# ]
