from django.urls import include, path

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import PostViewSet, CommentViewSet, FollowViewSet, GroupViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register(
    r'posts/(?P<post_id>[^/.]+)/comments',
    CommentViewSet,
    basename='comment'
)
router.register('follow', FollowViewSet, basename='follow')
router.register('group', GroupViewSet, basename='group')

urlpatterns = [
    path('', include(router.urls)),
    path(
        'token/',
        TokenObtainPairView.as_view(),
        name='token-obtain-pair-view'
    ),
    path(
        'token/refresh/',
        TokenRefreshView.as_view(),
        name='token-refresh-view'
    ),
]
