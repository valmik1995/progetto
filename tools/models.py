from django.db import models
from datetime import date
from django.contrib.auth.models import User
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File
from django.urls import reverse
import qrcode
import random

class QrCode(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    percorso=models.URLField()
    image=models.ImageField(upload_to='qrcode',default='path/to/my/default/image.jpg', blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def get_absolute_url(self):
        return reverse("tools:detail", kwargs={"id": self.id})

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)
