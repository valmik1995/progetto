from django.db import models

class Photo(models.Model):
    file = models.FileField(upload_to='photos/original')
    file_watermark = models.FileField(upload_to='photos/watermarks/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file

