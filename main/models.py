from django.db import models
from django.contrib.auth.models import User


# class User(AbstractUser):
#     manzil = models.CharField(max_length=255, blank=True, null=True)
#     tel = models.CharField(max_length=255, blank=True, null=True)
#     avatar = models.ImageField(max_length=255, blank=True, null=True, upload_to='avatar/')


class Region(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    banner_img = models.ImageField(upload_to='banner/')
    date = models.DateField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title


class PostImg(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='post-img/')


class PostVideo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    video = models.FileField(upload_to='post-video/')
    video_url = models.URLField(blank=True, null=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    body = models.TextField()
    is_show = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name