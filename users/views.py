from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import CustomUser
from .serializers import UserSerializer

# Perfil do usuário
class ProfileView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

# Seguir / deixar de seguir
class FollowToggleView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

    def post(self, request, *args, **kwargs):
        user_to_follow = self.get_object()
        current_user = request.user

        if user_to_follow == current_user:
            return Response({"detail": "Não é possível seguir a si mesmo."}, status=status.HTTP_400_BAD_REQUEST)

        if user_to_follow in current_user.following.all():
            current_user.following.remove(user_to_follow)
            action = 'unfollowed'
        else:
            current_user.following.add(user_to_follow)
            action = 'followed'

        current_user.save()
        serializer = self.get_serializer(user_to_follow, context={'request': request})
        return Response({'action': action, 'user': serializer.data})
