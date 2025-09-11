from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# Registro
def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("feed")
        else:
            messages.error(request, "Erro ao registrar. Verifique os dados.")
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})

# Perfil
def profile_view(request, username):
    profile_user = get_object_or_404(CustomUser, username=username)
    
    followers_count = profile_user.followers.count()  # quem segue este usuário
    following_count = profile_user.following.count()  # quem ele segue

    context = {
        "profile_user": profile_user,
        "followers_count": followers_count,
        "following_count": following_count,
    }
    return render(request, "profile.html", context)

# Seguir / deixar de seguir
@login_required
def follow_toggle(request, id):
    user_to_follow = get_object_or_404(CustomUser, id=id)
    current_user = request.user

    if user_to_follow != current_user:
        if user_to_follow in current_user.following.all():
            current_user.following.remove(user_to_follow)
        else:
            current_user.following.add(user_to_follow)
        current_user.save()
    
    return redirect('profile', username=user_to_follow.username)

class UsersListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = "users_list.html"
    context_object_name = "users"

# Lista de usuários para seguir
@login_required
def users_list(request):
    users = CustomUser.objects.exclude(id=request.user.id)
    return render(request, "users_list.html", {"users": users})
