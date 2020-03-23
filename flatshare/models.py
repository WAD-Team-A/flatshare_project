import uuid

from django.template.defaultfilters import slugify
from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
    generated_uuid = uuid.uuid4()
    address_id = models.UUIDField(primary_key=True, editable=False, default=generated_uuid)
    flat_no = models.CharField(max_length=5)
    house_no = models.IntegerField(default=1)
    street = models.CharField(max_length=99)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    postcode = models.CharField(max_length=10)
    country = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return self.flat_no + ' ' + str(self.house_no) + ' ' + self.street + ' ' + self.city + ' ' + self.province


class Flat(models.Model):
    NAME_MAX_CHAR = 128
    name = models.CharField(max_length=NAME_MAX_CHAR)
    generated = uuid.uuid4()
    flat_id = models.UUIDField(primary_key=True, editable=False, default=generated)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)
    rent = models.IntegerField(default=1)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    description = models.TextField(max_length=500)
    available_from = models.DateField(default=now)
    save_location: str = '{0}_images/'.format(generated)
    image1 = models.ImageField(upload_to=save_location, blank=True, null=True)
    image2 = models.ImageField(upload_to=save_location, blank=True, null=True)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.generated)
        super(Flat, self).save(*args, **kwargs)

    def __str__(self):
        return self.name + ' ' + str(self.address)


class UserProfile(models.Model):
    NAME_MAX_CHAR = 128
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=NAME_MAX_CHAR, unique=False)
    LastName = models.CharField(max_length=NAME_MAX_CHAR, unique=False)
    picture = models.ImageField(upload_to='{0}/profile_images'.format(id(user)), blank=True)
    phone_no = models.IntegerField(default=888, unique=True)
    age = models.IntegerField(default=18)
    liked_flats = models.ManyToManyField(Flat, related_name="likers", blank=True)
    slug = models.SlugField(blank=True)

    # owned_flats: get via flats model

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user)
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.FirstName + " " + self.LastName
