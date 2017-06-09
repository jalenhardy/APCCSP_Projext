from django.db import models


class Victim(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    bio = models.TextField()
    source = models.CharField(max_length=500)
    date_recieved = models.DateField()
    big_photo = models.TextField()
    youtube_source = models.CharField(max_length=1000)
    photo_1 = models.CharField(max_length=1000)
    protest_photo = models.CharField(max_length=1000,
                                     default='http://a.abcnews.com/images/International/EPA_blm_south_africa_01_as_160713_4x3_992.jpg')
