from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import UsersListView, follow_toggle

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", auth_views.LoginView.as_view(
        template_name="login.html", 
        redirect_authenticated_user=True
    ), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    path("profile/<str:username>/", views.profile_view, name="profile"),
    path("follow/<int:id>/", follow_toggle, name="follow-toggle"),
    path("users/", views.users_list, name="users-list"),
]
