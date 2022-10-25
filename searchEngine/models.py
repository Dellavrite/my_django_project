from django.db import models


# Create your models here.

class News(models.Model):
    post_link = models.CharField(max_length=255)
    post_name = models.CharField(max_length=255)
    sender_name = models.CharField(max_length=31)
    sender_link = models.CharField(max_length=255)
    post_date = models.DateField()
    post_id = models.CharField(max_length=63)


