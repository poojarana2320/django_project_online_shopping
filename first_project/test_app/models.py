from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Author(models.Model):
    '''This is Author class that contains Authors information'''
    first_name=models.CharField(max_length=30)
    lat_name=models.CharField(max_length=30,blank=True)
    Email=models.EmailField(unique=True)
    age=models.IntegerField()
    Gender_Choices=(
        ('M','Male'),
        ('F','Female')
        )
    gender=models.CharField(max_length=1 , choices=Gender_Choices)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Author'
    def __str__(self):
        return '%s %s' %(self.first_name,self.lat_name)

class Publisher(models.Model):
    ''' This is Publisher class that contains publisher information'''

    Name=models.CharField(max_length=30)
    Address=models.TextField(max_length=50)
    City=models.CharField(max_length=50)
    State=models.CharField(max_length=50)
    Country=models.CharField(max_length=50)
    Website=models.URLField()

    class Meta:
        unique_together = ('Name', 'Address',)
    def __str__(self):
        return self.Name

class Book(models.Model):
    '''This is book class that contain books informatins.'''
    Title=models.CharField(max_length=30 ,blank=True,unique=True)
    Publishers=models.ForeignKey(Publisher , on_delete=models.CASCADE)
    Authors=models.ManyToManyField(Author)  
    Publications_date=models.DateField(null=True)   

    def __str__(self):
        return self.Title