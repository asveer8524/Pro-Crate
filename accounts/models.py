from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
TYPE=(("Student","Student"),
       ("Faculty","Faculty"),
       ("Other","Other"))

class Profile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=60)
    city = models.CharField(max_length=40)
    email = models.EmailField()
    department = models.CharField(max_length=40)
    mobile_no = models.CharField(max_length=12)
    profile_pic = models.ImageField(default='def_user.svg')
    type = models.CharField(max_length=20, choices=TYPE, default="Other")
    def __str__(self):
        return self.username
