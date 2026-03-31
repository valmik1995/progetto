import os
import qrcode
import re
import random
from django.db.models.signals import pre_save
from django.dispatch import receiver
from tools.models import QrCode
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File


@receiver(pre_save, sender=QrCode)
def creare_qrcode(instance, **kwargs):
    if instance._state.adding:
        img=qrcode.make(instance.percorso)
        qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10, border=4,)
        qr.add_data(instance.percorso)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
        title = re.sub('[^A-Za-z0-9]+', '', instance.title)
        name = 'media/qrcode/' + title + '_qrcode_' + str(random.randint(0,9999)) + '.png'
        img.save(name)
        instance.image = name.replace('media/', '')
    else:
        pass

