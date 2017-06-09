from django.db import models


class Activist(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    bio = models.TextField()
    source = models.CharField(max_length=500)
    date_recieved = models.DateField()
    photo = models.TextField()
    photos = models.TextField(default="None")
    twitter_name = models.TextField(default="@Blklivesmatter")
    youtube = models.CharField(default="None", max_length=5000)
    quotes = models.TextField(default="None")


