from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser, Follow
from .serializers import UserSerializer

# Lista de quem o usuário segue
class FollowingListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        return CustomUser.objects.filter(
            id__in=Follow.objects.filter(user_id=user_id).values("followed_user")
        )

# Lista de seguidores do usuário
class FollowersListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        return CustomUser.objects.filter(
            id__in=Follow.objects.filter(followed_user_id=user_id).values("user")
        )
