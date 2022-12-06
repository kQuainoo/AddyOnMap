
from django.db import models
# from django.contrib import admin    
# import datetime
# from django.utils import timezone

# table UserRadius with a few fields.

class UserRadius(models.Model):

    uRadius_text = models.BigIntegerField
    city = models.CharField(max_length = 200)
    province = models.CharField(max_length = 100)
    pub_date = models.DateTimeField('This is the date of request')

    # @admin.display(
    #     boolean=True,
    #     ordering='pub_date',
    #     description='this is text right here?'
    # )
    def __str__(self) -> str:
        return self.uRadius_text

