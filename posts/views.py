from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# API: Posts
class PostListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# API: Curtir/descurtir post
class LikePostView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']
        post = get_object_or_404(Post, id=post_id)
        like, created = Like.objects.get_or_create(post=post, user=self.request.user)
        if not created:
            like.delete()  # descurtir se já tiver

# API: Comentários
class CommentPostView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']
        post = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=post)

# Front-end: Feed
@login_required
def feed_view(request):
    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            Post.objects.create(author=request.user, content=content)
            return redirect("feed")  # evita repostar ao dar refresh

    following_users = request.user.following.values_list("id", flat=True)
    posts = Post.objects.filter(author__in=list(following_users) + [request.user.id]).order_by("-created_at")

    return render(request, "feed.html", {"posts": posts})

# Like por formulário HTML
@login_required
@require_POST
def like_post_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(post=post, user=request.user)
    if not created:  # se já existe, descurte
        like.delete()
    return redirect("feed")

# Comentar por formulário HTML
@login_required
@require_POST
def comment_post_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    content = request.POST.get("content")
    if content:
        Comment.objects.create(post=post, author=request.user, content=content)
    return redirect("feed")
