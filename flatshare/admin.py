from django.contrib import admin
from flatshare.models import Flat, User_addFlat, User_findFlat, Profile_addFlat, Address, Flat_images


admin.site.register(Flat)
admin.site.register(Profile_addFlat)
admin.site.register(User_addFlat)
admin.site.register(User_findFlat)
admin.site.register(Address)
admin.site.register(Flat_images)

# Register your models here.
