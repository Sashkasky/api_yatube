from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from api.views import CommentViewSet, GroupViewSet, PostViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='group')
router.register(r'posts/(?P<post_id>[^/.]+)/comments',
                CommentViewSet, basename='comments')

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]
