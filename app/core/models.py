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


class Recipe(models.Model):
    """Recipe object."""
    user= models.ForeignKey(
        settings.Auth_user_Model,
        on_delete = models.CASCADE,
    )
    title=models.CharField(max_length=255)
    description = models.TextField(blank=True)
    time_minutes = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    link= models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title