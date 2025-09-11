from django.urls import path
from .views import PostListCreateView, LikePostView, CommentPostView, feed_view

urlpatterns = [
    path('', PostListCreateView.as_view(), name='post-list-create'),  # API
    path('<int:post_id>/like/', LikePostView.as_view(), name='like-post'),  # API
    path('<int:post_id>/comments/', CommentPostView.as_view(), name='comment-post'),  # API
    path('feed/', feed_view, name='feed'),  # Front-end
]