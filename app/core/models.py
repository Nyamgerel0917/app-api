"""
Database models
"""
from django.db import models  # noqa
from django.contrib.auth.models import(
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_field):
        """Create, saved and return a new user"""
        if not email: 
            raise ValueError('User must have an emial address.')
        user = self.model(email=self.normalize_email(email),**extra_field)
        user.set_password(password)
        user.save(using=self._db)

        return user 


    def create_superuser(self, email, password):
        """Create and"""
class User(AbstractBaseUser,PermissionsMixin):
    """User in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'