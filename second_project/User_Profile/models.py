
from __future__ import unicode_literals
import os
from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django_countries import countries


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

"""Registration table of User"""


class Registration(models.Model):
    # username=models.CharField(max_length=50)
    # fullname=models.CharField(max_length=50)
    # email=models.EmailField()
    # password=models.CharField(max_length=50)
    # confirmpassword=models.CharField(max_length=50)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    mobileno = models.CharField(max_length=10)
    address = models.TextField(max_length=50)
    profile_image = models.ImageField(upload_to="images/", blank=True, null=True)
    country = CountryField(choices=list(countries))

    def __str__(self):
        return self.user_id.username


"""Shopping cart Product table"""


class Product(models.Model):
    # name=models.OneToOneField(User,on_delete=models.CASCADE)
    prodcut_name = models.CharField(max_length=50)
    price = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    picture = models.ImageField(null=True, upload_to='images/')

    def __str__(self):
        return self.prodcut_name

""" Cart table """


class Cart(models.Model):
    state_option = (
        ('c', 'Confirm'),
        ('d', 'Draft')
        )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.PositiveSmallIntegerField(default=0)
    state = models.CharField(max_length=10, choices=state_option, default='d')

    def __str__(self):
        return self.user.email

""" Cartitems table """


class CartItem(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.item.prodcut_name
