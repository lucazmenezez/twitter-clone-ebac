from django.urls import path
from .views import (
    PostListCreateView, LikePostView, CommentPostView, feed_view,
    like_post_view, comment_post_view
)

urlpatterns = [
    # API
    path('', PostListCreateView.as_view(), name='post-list-create'),
    path('<int:post_id>/like/', LikePostView.as_view(), name='like-post'),
    path('<int:post_id>/comments/', CommentPostView.as_view(), name='comment-post'),

    # Front-end
    path('feed/', feed_view, name='feed'),
    path('feed/<int:post_id>/like/', like_post_view, name='like-post-html'),
    path('feed/<int:post_id>/comment/', comment_post_view, name='comment-post-html'),
]