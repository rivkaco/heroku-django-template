import datetime
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from datetime import date
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.CharField(max_length= 500)
    title = models.CharField(max_length=500)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=date.today())
    # published_date = models.DateTimeField(
    #     blank=True, null=True)

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def __str__(self):
        return self.title
    #
    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

