from django.db import models
from django.contrib import admin  

# import datetime
# from django.utils import timezone

# table UserRadius with a few fields.
# TODO insert data into addy table from django admin site

class addy(models.Model):
    addy_text = models.CharField('Place of Interest',max_length=200)
    object_id = models.IntegerField()


    def __str__(self):
        return '%s %s' % (self.addy_text, 'Place of Interest')
        


class UserRadius(models.Model):

    uRadius_text = models.BigIntegerField(default=2)
    uinput_rad = models.BooleanField()
    uRadius_text = models.ForeignKey(addy,on_delete=models.CASCADE)
    # uRadius_date = models.DateField(default=date.today)

    def __str__(self) -> str:
        return self.uRadius_text
