from django.db import models
from django.contrib.auth .models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class DesignCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='categoryPicture', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Design Category'
        verbose_name_plural = 'Design Categories'

    def __str__(self):
        return self.name


class Design(models.Model):
    picture = models.ImageField(upload_to='design', null=True, blank=True)
    category = models.ForeignKey(DesignCategory, on_delete=models.CASCADE, related_name='designs')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Designs'

    

