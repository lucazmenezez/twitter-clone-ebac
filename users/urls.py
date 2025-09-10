from django.urls import path
from .views import ProfileView, FollowToggleView

urlpatterns = [
    path('profile/<int:id>/', ProfileView.as_view(), name='profile'),
    path('follow/<int:id>/', FollowToggleView.as_view(), name='follow-toggle'),
]
