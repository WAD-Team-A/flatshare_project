from django.contrib import admin
from flatshare.models import *

admin.site.register(Flat)
admin.site.register(UserProfile)
admin.site.register(Address)
admin.site.register(FlatImageGallery)

# Register your models here.
