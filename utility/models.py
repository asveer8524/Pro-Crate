from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from projects.models import project_data
# Create your models here.


class bookmarks(models.Model):
    bookmark_slug = models.ForeignKey(project_data, on_delete=models.CASCADE)
    slug = models.SlugField()
    bookmark_title = models.CharField(max_length=100, primary_key=True)
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    owner = models.CharField(max_length=100)

    def __str__(self):
        return self.bookmark_title

class comments(models.Model):
    comment_field = models.TextField()
    comment_on_slug = models.SlugField()
    comment_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    owner = models.CharField(max_length=100)
    comment_date = models.DateTimeField(auto_now_add=True)
