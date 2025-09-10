from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer

# Posts
class PostListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# Curtir post
class LikePostView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        post_id = self.request.data.get('post')
        like, created = Like.objects.get_or_create(post_id=post_id, user=self.request.user)
        if not created:
            like.delete()  # descurtir se já tiver

# Comentar post
class CommentPostView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']
        serializer.save(author=self.request.user, post_id=post_id)

class FeedView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        # pega todos os usuários que o usuário atual segue
        following_users = user.following.all()
        # filtra posts desses usuários
        return Post.objects.filter(author__in=following_users).order_by('-created_at')
