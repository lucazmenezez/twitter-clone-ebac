from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=150, blank=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    following = models.ManyToManyField(
        'self',
        symmetrical=False,  # não é recíproco
        related_name='followers',
        blank=True
    )

    def __str__(self):
        return self.username