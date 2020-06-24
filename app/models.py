from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    creation_date = models.DateTimeField(auto_now_add=True)
    amount_of_upvotes = models.PositiveIntegerField(default=0)
    author_name = models.CharField(max_length=255)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author_name = models.CharField(max_length=255)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
