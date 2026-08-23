from django.db import models
from django.conf import settings


class Profile(models.Model):
    """
    Profile model that extends Django's User model.
    It adds two fields:
     - date_of_birth
     - photo
    Field user utilize data from Django's User model and store reference to it.
    Using AUTH_USER_MODEL make code more generic - it can work with custom User model either.
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)


    def __str__(self):
        return f'Profile of {self.user.username}'
