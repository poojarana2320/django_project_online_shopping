from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.utils.timezone import now

# Create your models here.

class Restaurant_review(models.Model):
    Name=models.CharField(max_length=50,verbose_name='Name')
    Email_id=models.EmailField()
    Age=models.IntegerField()
    Feedback=models.TextField(max_length=50)
    food_Quality=(
        ('excellent','Excellent'),
        ('good','Good'),
        ('average','Average'),
        ('dissatisfied','Dissatisfied')
        )
    Food_Quality=models.CharField(max_length=12 , choices=food_Quality)

    Location_Choices=(
        ('Location1','Location1'),
        ('Location2','Location2'),
        ('Location3','Location3')
        )
    Location_Visited=models.CharField(max_length=9 , choices=Location_Choices)

    def __str__(self):
        return self.Name

class bookingAirTicket(models.Model):
    Name=models.CharField(max_length=50)
    Email_id=models.EmailField()
    Age=models.IntegerField()
    Address=models.TextField(max_length=100)
    Mobile=models.CharField(max_length=15)
    Travel_From_Date = models.DateTimeField(default=now)
    Travel_To_Date = models.DateTimeField(default=now)
    Travel_From = models.CharField(max_length=50)
    Travel_To = models.CharField(max_length=50)
    No_of_person=models.IntegerField()

    def __str__(self):
        return self.Name

class Categoreis(models.Model):
    Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Name




