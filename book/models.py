from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipe_post')
    date_posted = models.DateTimeField(auto_now_add=True)
    ingredients = models.TextField()
    method = models.TextField()
    recipe_image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(User, related_name='recipe_likes', blank=True)
    shares = models.ManyToManyField(User, related_name='share', blank=True)


class Meta:
    ordering = ['-date_posted']


def __str__(self):
    return self.title


def number_of_likes(self):
    return self.likes.count()


def number_of_shares(self):
    return self.shares.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["date_posted"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
