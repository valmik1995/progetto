from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(LeafletGeoAdmin):
    list_display = ("id", "user", "qualifica", "address", "profile_pic", "geom")