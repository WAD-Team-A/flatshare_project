import uuid
from pathlib import Path

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

    # owned_flats: get via flats model
    # liked_flats = models.ManyToManyField(Flat)

    def __str__(self):
        return self.FirstName + " " + self.LastName


class Address(models.Model):
    address_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    flat_no = models.CharField(max_length=5)
    house_no = models.IntegerField(default=1)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    postcode = models.CharField(max_length=10)
    country = models.CharField(max_length=60)

    def __str__(self):
        return self.flat_no + ' ' + str(self.house_no) + ' ' + self.street + ' ' + self.city + ' ' + self.province


class FlatImageGallery(models.Model):
    def __init__(self, flat_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        save_location: str = '/home/meta4icalbot/' + str(flat_id) + '_images'
        Path(save_location).mkdir(parents=True, exist_ok=True)
        # gallery = []
        # for i in range(5):
        #   gallery.append(models.ImageField(upload_to=save_location, blank=True, null=True))
        self.image1 = models.ImageField(upload_to=save_location, blank=True, null=True)
        self.image2 = models.ImageField(upload_to=save_location, blank=True, null=True)
        self.image3 = models.ImageField(upload_to=save_location, blank=True, null=True)
        self.image4 = models.ImageField(upload_to=save_location, blank=True, null=True)


class Flat(models.Model):
    NAME_MAX_CHAR = 128
    name = models.CharField(max_length=NAME_MAX_CHAR)
    flat_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)
    rent = models.IntegerField(default=1)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    description = models.TextField(max_length=500)
    available_from = models.DateField(default=now)
    images = models.OneToOneField(FlatImageGallery(flat_id), on_delete=models.SET_NULL, null=True, blank=True)

    # likers = models.ManyToManyField(User)

    def __str__(self):
        return self.name + ' ' + str(self.address)