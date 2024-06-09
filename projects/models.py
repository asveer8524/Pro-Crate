from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile

# Create your models here.

#comment bookmark like


class project_data(models.Model):
    title = models.CharField(max_length=100, primary_key=True)
    abstract = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique = True)
    files = models.FileField(blank = True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    owner1 = models.CharField(default = 'None', max_length=120)
    category = models.CharField(max_length=150)
