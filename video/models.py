import re
from django.db import models
from django.urls import reverse

class Video(models.Model):
    FORMATO_VIDEO_CHOICES = (
    ("640", "640"),
    ("1280", "720"),
    ("1920", "1080"),
    )
    POSIZIONE_VIDEO_CHOICES = (
    ("VERT", "Verticale"),
    ("ORIZ", "Orizzontale"),
    )
    CODINO_CHOICES = (
    ("SENZA", "Senza"),
    ("CODIN", "Codino"),
    )
    LOGO_CHOICES = (
    ("SENZ", "Senza"),
    ("LOGO", "Logo"),
    )

    title   = models.CharField(max_length=120)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    formato = models.CharField(max_length=4, choices=FORMATO_VIDEO_CHOICES, default=1280)
    posizione = models.CharField(max_length=4, choices=POSIZIONE_VIDEO_CHOICES, default='ORIZ')
    codino = models.CharField(max_length=5, choices=CODINO_CHOICES, default='CODIN')
    logo = models.CharField(max_length=4, choices=LOGO_CHOICES, default='LOGO')
    video = models.FileField(upload_to='video/original', max_length=500)
    video_watermarks = models.FileField(upload_to='video/watermarks',max_length=500, blank=True, null=True)

    def get_absolute_url(self):
        return reverse("video:video-detail", kwargs={"id": self.id})

    def __str__(self):
        return self.title
    
 
    def delete(self, *args, **kwargs):
        self.video.delete()
        self.video_watermarks.delete()
        super().delete(*args, **kwargs)
