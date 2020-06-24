from __future__ import absolute_import, unicode_literals
from celery import task
from app.models import Post


@task()
def reset_post_upvotes_count():
    """task for reset post upvotes count"""
    Post.objects.update(amount_of_upvotes=0)
