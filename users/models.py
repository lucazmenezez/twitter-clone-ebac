from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    following = models.ManyToManyField(
        'self',
        symmetrical=False,  # não é recíproco: A segue B ≠ B segue A
        related_name='followers',  # usuários que seguem este usuário
        blank=True
    )

    def __str__(self):
        return self.username
