from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Listing(models.Model):
    # each listing is connected w/ an authenticated user
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    # todo: take from car table car_year, car_make, car_model, car_category
    car = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    borough = models.CharField(max_length=100)
    price = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    is_rented = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
