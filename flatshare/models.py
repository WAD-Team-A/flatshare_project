import uuid

from django.template.defaultfilters import slugify
from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
    address_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
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
    flat_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)
    rent = models.IntegerField(default=1)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None, related_name="owned_flat_set")
    description = models.TextField(max_length=500)
    available_from = models.DateField(default=now)
    save_location: str = '{0}_images/'.format(flat_id)
    image1 = models.ImageField(upload_to=save_location, blank=True, null=True)
    image2 = models.ImageField(upload_to=save_location, blank=True, null=True)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.flat_id)
        super(Flat, self).save(*args, **kwargs)

    def __str__(self):
        return self.name + ' ' + str(self.address)


class UserProfile(models.Model):
    NAME_MAX_CHAR = 128
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=NAME_MAX_CHAR, unique=False)
    LastName = models.CharField(max_length=NAME_MAX_CHAR, unique=False)
    picture = models.ImageField(upload_to='{0}/profile_images'.format(id(user)), blank=True)
    phone_no = models.IntegerField(unique=True, blank=True)
    bio = models.CharField(max_length=500,unique=False,default="")
    age = models.IntegerField(default=18)
    liked_flats = models.ManyToManyField(Flat, related_name="likers", blank=True)
    liked_users = models.ManyToManyField(User, related_name="liked_by_set", blank=True)
    slug = models.SlugField(blank=True)

    # owned_flat_set: get via flats model

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user)
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.FirstName + " " + self.LastName

class Match(models.Model):
    match_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    m_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    m_flat = models.ForeignKey(Flat, on_delete=models.CASCADE, related_name='+')
    m_owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='+', null=True)

    class Meta:
        verbose_name_plural = 'Matches'

    def __str__(self):
        return str(self.m_user) + " " + str(self.m_flat)
