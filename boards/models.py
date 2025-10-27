from django.db import models
# auth is already exist in django framework
from django.contrib.auth.models import User
from django.utils.text import Truncator


# Create your models here.
class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=180)

    def __str__(self):
        return self.name

    def get_posts_count(self):
        return Post.objects.filter(topic__board=self).count()

    def get_last_post(self):
        return Post.objects.filter(topic__board=self).order_by('-create_dt').first()


class Topic(models.Model):
    subject = models.CharField(max_length=250)
    board = models.ForeignKey(
        Board, related_name="topics", on_delete=models.CASCADE)     # one-to-many relation with Board
    created_by = models.ForeignKey(
        User, related_name="topics", on_delete=models.CASCADE)     # one-to-one relation with User
    create_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


class Post (models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(
        Topic, related_name="posts", on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        User, related_name="posts", on_delete=models.CASCADE)
    create_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        truncated_message = Truncator(self.message)
        return truncated_message.chars(40)
