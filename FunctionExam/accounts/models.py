from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
from django.db.models.signals import post_save
from django.dispatch import receiver
from uuid import uuid4
from datetime import datetime, timedelta

# Create your models here.
class Users(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    picture = models.FileField(null=True, upload_to='picture/')

    USERNAME_FIELD = "email"
    REQUIRED_FIELD = ["username"]

    class Meta:
        db_table = "users"

class UserActivateToken(models.Model):
    token = models.UUIDField(db_index=True)
    expired_at = models.DateTimeField()
    user = models.ForeignKey(
        "users", on_delete=models.CASCADE
    )

    class Meta:
        db_table = "user_active_tokens"

@receiver(post_save, sender=Users)
def publish_token(sender, instance, **kwargs):
    print(uuid4())
    print(datetime.now + timedelta(days=1))
    user_activate_token = UserActivateToken.objects.create(
        user = instance,
        token = str(uuid4()),
        expired_at = datetime.now + timedelta(days=1)
    )
    print(f'http://127.0.0.1:8000/accounts/activate_user/{user_activate_token}')