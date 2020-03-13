from django.db import models
from django.contrib.auth.models import User






class Profile(models.Model):
    NAME_MAX_CHAR = 128
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    FirstName = models.CharField(max_length = NAME_MAX_CHAR, unique = False)
    LastName = models.CharField(max_length= NAME_MAX_CHAR, unique = False)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    phone_no = models.IntegerField(default = 888, unique = True)
    age = models.IntegerField(default = 18)
    def __str__(self):
        return (self.FirstName + " "+ self.LastName)

class Flat(models.Model):
    NAME_MAX_CHAR = 128
    flat_id = models.IntegerField(default = 1, primary_key=True)
    rent = models.IntegerField(default = 1)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    street = models.CharField(max_length = NAME_MAX_CHAR, unique = False)
    house_no = models.CharField(max_length = 50, unique = False)
    postCode = models.CharField(max_length = 50, unique = False)
    city = models.CharField(max_length = 128, unique = False)
    def __str__(self):
        return self.flat_id


# Create your models here.
