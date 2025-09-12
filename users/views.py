from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CustomUserCreationForm, UserUpdateForm, CustomPasswordChangeForm
from .models import CustomUser


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

    followers_count = profile_user.followers.count()
    following_count = profile_user.following.count()

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

    return redirect('profile', username=user_to_follow.username)


class UsersListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = "users_list.html"
    context_object_name = "users"


@login_required
def users_list(request):
    users = CustomUser.objects.exclude(id=request.user.id)
    return render(request, "users_list.html", {"users": users})


@login_required
def edit_profile(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil atualizado com sucesso!")
            return redirect("profile", username=request.user.username)
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, "users/edit_profile.html", {"form": form})


@login_required
def change_password(request):
    if request.method == "POST":
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # mantém logado
            messages.success(request, "Senha alterada com sucesso!")
            return redirect("profile", username=request.user.username)
    else:
        form = CustomPasswordChangeForm(request.user)

    return render(request, "users/change_password.html", {"form": form})
