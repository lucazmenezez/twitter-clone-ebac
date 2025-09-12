from django.contrib import admin
from django.urls import path, include
from posts.views import feed_view
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView  # <--- import necessário

urlpatterns = [
    path("admin/", admin.site.urls),

    # autenticação
    path("register/", user_views.register_view, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),

    # feed + perfil
    path("feed/", feed_view, name="feed"),
    path("profile/<str:username>/", user_views.profile_view, name="profile"),

    # redirecionar raiz para login
    path("", RedirectView.as_view(url="/login/", permanent=False)),

    # incluir urls dos apps
    path('posts/', include('posts.urls')),
    path('users/', include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
