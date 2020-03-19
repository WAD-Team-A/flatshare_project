from django.contrib import admin
from flatshare.models import Flat, UserProfile, Address, FlatImages

admin.site.register(Flat)
admin.site.register(UserProfile)
admin.site.register(Address)
admin.site.register(FlatImages)

# Register your models here.
