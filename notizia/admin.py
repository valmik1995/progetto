from django.contrib import admin
from .models import Notizia, Images, VideoNotizia
from . import forms


@admin.register(Notizia)
class NotiziaAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'comune', 'slug', 'date']
    list_display = ("title", "comune", "slug")


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ("note_id", "image")

@admin.register(VideoNotizia)
class VideoNotiziaAdmin(admin.ModelAdmin):
    list_display = ("note_id", "video")




# class NotiziaInline(admin.TabularInline):
#     model = Notizia
#
# class ImagesAdmin(admin.ModelAdmin):
#     inlines = [
#         NotiziaInline,
#     ]

# @admin.register(models.Notizia)
# class NotiziaAdmin(admin.ModelAdmin):
#     form = forms.NotiziaFullForm
#
#
# @admin.register(models.Country)
# class CountryAdmin(admin.ModelAdmin):
#     model = models.Country
