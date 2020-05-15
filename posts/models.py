from django.db import models
from accounts.models import UserProfile
from django.utils import timezone
from autoslug import AutoSlugField


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_image = models.ImageField(blank=True, upload_to='post_pics')
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_date = models.DateField(default=timezone.now)
    slug = AutoSlugField(populate_from='title')

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField(max_length=250, verbose_name='Comment')
    created_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:10]
