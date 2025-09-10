from django.urls import path
from .views import FollowingListView, FollowersListView

urlpatterns = [
    path("<int:user_id>/following/", FollowingListView.as_view(), name="user-following"),
    path("<int:user_id>/followers/", FollowersListView.as_view(), name="user-followers"),
]
