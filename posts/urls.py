from django.urls import path
from .views import PostListCreateView, LikePostView, CommentPostView

urlpatterns = [
    path('', PostListCreateView.as_view(), name='post-list-create'),
    path('like/', LikePostView.as_view(), name='like-post'),
    path('<int:post_id>/comments/', CommentPostView.as_view(), name='comment-post'),
]
