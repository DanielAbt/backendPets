from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


# Create your models here.

class CustomUserManager(BaseUserManager): 
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames. 
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_admin=True.'))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    #objects = CustomUserManager()
    
    # def __str__(self):
    #     return self.email

class Pets(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=40, null=False)
    is_birth_approximate = models.BooleanField(null=False)
    birth_date = models.DateField(null=False)

    class Meta:
        managed = True
        db_table = 'Pets'
        # uncomment the following line to use name and date of birth as key, you need to run makemigrations and migrate.
        # unique_together = (('name', 'birth_date'),)