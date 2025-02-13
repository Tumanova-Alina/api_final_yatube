from django.urls import include, path
from rest_framework import routers

from api.views import PostViewSet, CommentViewSet, FollowViewSet, GroupViewSet

router_v1 = routers.DefaultRouter()
router_v1.register('posts', PostViewSet)
router_v1.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet, basename='comments')
router_v1.register('groups', GroupViewSet)
router_v1.register('follow', FollowViewSet, basename='followers')

api_v1_patterns = [
    path('', include(router_v1.urls)),
    path('', include('djoser.urls.jwt')),
]

urlpatterns = [
    path('v1/', include(api_v1_patterns)),
]
