from django.db import models
# auth is already exist in django framework
from django.contrib.auth.models import User


# Create your models here.
class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=180)


class Topic(models.Model):
    subject = models.CharField(max_length=250)
    board = models.ForeignKey(
        Board, related_name="topics", on_delete=models.CASCADE)     # one-to-many relation with Board
    created_by = models.ForeignKey(
        User, related_name="topics", on_delete=models.CASCADE)     # one-to-one relation with User
    created_dt = models.DateTimeField(auto_now_add=True)


class Post (models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(
        Topic, related_name="posts", on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        User, related_name="posts", on_delete=models.CASCADE)
    create_dt = models.DateTimeField(auto_now_add=True)
