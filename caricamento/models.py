from django.db import models

class Caricamento(models.Model):
    titolo = models.CharField(max_length=255, blank=True)
    photos = models.FileField(upload_to='photos/')
    photos_watermark = models.FileField(upload_to='watermarks/')
    aggiornamento = models.DateTimeField(auto_now_add=True)


class FilesUploads(models.Model):
    file_field= models.FileField()
