import sys
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import NullBooleanField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.core.validators import RegexValidator
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

class Profile(models.Model):
    QUALIFICA_CHOICES = [
        ('VP', 'Vigile Permanete'),
        ('VE', 'Vigile Esperto'),
        ('VC', 'Vigile Coordinatore'),
        ('CS', 'Capo Squadra'),
        ('CSE', 'Capo Squadra Esperto'),
        ('CR', 'Capo Reparto'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    qualifica = models.CharField(max_length=3, choices=QUALIFICA_CHOICES,default='VP')
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=255, blank=True)
    comando = models.CharField(max_length=150, blank=True)
    phone_regex = RegexValidator(regex=r'^(\+\d{1,3})?,?\s?\d{8,13}', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    geom = models.PointField(geography=True, default=Point(12.596318720019047, 44.03671715457052, srid=4326), spatial_index=True, null=True,blank=True)
    profile_pic = models.ImageField(upload_to='profile', default="profile/user.png", null=True, blank=True)
    email = models.EmailField(max_length=150)
    signup_confirmation = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    @property
    def lat_lng(self):
        return list(getattr(self.geom, 'coords', [])[::-1])
    
    def compressImage(self,profile_pic):
        basewidth = 200
        imageTemproary = Image.open(profile_pic)
        imageTemproary = imageTemproary.convert('RGB')
        outputIoStream = BytesIO()
        wpercent = (basewidth/float(imageTemproary.size[0]))
        hsize = int((float(imageTemproary.size[1])*float(wpercent)))
        imageTemproaryResized = imageTemproary.resize((basewidth,hsize), Image.LANCZOS)
        imageTemproaryResized.save(outputIoStream , format='JPEG', quality=60)
        outputIoStream.seek(0)
        profile_pic = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % profile_pic.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        return profile_pic
    
    def save(self, *args, **kwargs):
        if self.profile_pic:
            self.profile_pic = self.compressImage(self.profile_pic)
            super(Profile, self).save(*args, **kwargs)
        else:
            self.profile_pic = self.profile_pic
            super(Profile, self).save(*args, **kwargs)

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
