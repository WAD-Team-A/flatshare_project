from django.db import models
from django.contrib.auth.models import User


class User_addFlat(models.Model):
    MAX_CHAR = 128
    username = models.CharField(max_length = MAX_CHAR, unique = True)
    password_addFlat = models.CharField(max_length = MAX_CHAR, unique = False)
    email_addflat = models.CharField(max_length = MAX_CHAR, unique = True)

class User_findFlat(models.Model):
    MAX_CHAR = 128
    username = models.CharField(max_length = MAX_CHAR, unique = True)
    password_findflat = models.CharField(max_length = MAX_CHAR, unique = False)
    email_findflat = models.CharField(max_length = MAX_CHAR, unique = True)



class Profile_addFlat(models.Model):
    NAME_MAX_CHAR = 128
    user = models.OneToOneField(User_addFlat, on_delete=models.CASCADE)
    FirstName = models.CharField(max_length = NAME_MAX_CHAR, unique = False)
    LastName = models.CharField(max_length= NAME_MAX_CHAR, unique = False)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    phone_no = models.IntegerField(default = 888, unique = True)
    age = models.IntegerField(default = 18)
    def __str__(self):
        return (self.FirstName + " "+ self.LastName)

class Flat(models.Model):
    NAME_MAX_CHAR = 128
    rent = models.IntegerField(default = 1)
    addflat_user = models.OneToOneField(User_addFlat, on_delete = models.CASCADE)

    def __str__(self):
        return self.flat_id


class Address(models.Model):
    MAX_CHAR = 128
    flat = models.OneToOneField(Flat, on_delete = models.CASCADE)
    street = models.CharField(max_length =MAX_CHAR, unique = False)
    house_no = models.CharField(max_length = 50, unique = False)
    postCode = models.CharField(max_length = 50, unique = False)
    city = models.CharField(max_length = 128, unique = False)

class Flat_images(models.Model):
    iamge_flat = models.ForeignKey(Flat, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='flat_images', blank=True)


# Create your models here.
