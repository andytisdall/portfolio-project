from django.contrib import admin

# Register your models here.
from .models import Lyrics, Album, Appearance

admin.site.register(Lyrics)
admin.site.register(Album)
admin.site.register(Appearance)
