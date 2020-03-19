from django.contrib import admin
from flatshare.models import Flat, UserProfile, Address

admin.site.register(Flat)
admin.site.register(UserProfile)
admin.site.register(Address)

# Register your models here.
