import uuid
from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    NAME_MAX_CHAR = 128
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=NAME_MAX_CHAR, unique=False)
    LastName = models.CharField(max_length=NAME_MAX_CHAR, unique=False)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    phone_no = models.IntegerField(default=888, unique=True)
    age = models.IntegerField(default=18)
   #liked_flats = models.ManyToManyField(Flat)

    def __str__(self):
        return self.FirstName + " " + self.LastName


class Address(models.Model):
    flat_no = models.CharField(max_length=5)
    house_no = models.IntegerField()
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    postcode = models.CharField(max_length=10)
    country = models.CharField(max_length=60)

class Flat(models.Model):
    name = models.CharField(max_length=30)
    flat_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4())
    address = Address
    rent = models.IntegerField(default=1)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    available_from = models.DateField(default=now)
    image = models.ImageField(upload_to=str(flat_id)+'_images', blank=True) #will be replaced by a gallery soon

   #likers = models.ManyToManyField(User)

    def __str__(self):
        return self.flat_id + self.address
