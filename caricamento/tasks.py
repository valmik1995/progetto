from __future__ import absolute_import, unicode_literals
import os
import time
import subprocess
from celery import shared_task, current_task
from django.conf import settings
from caricamento.models import Caricamento
from PIL import Image
from time import sleep



@shared_task(bind=True)
def process_file(self, photos_name):
    image = Image.open(photos_name).convert("RGBA")
    watermark = Image.open('/home/adirimini/vpodrini/project/media/watermarks/IMG_4156.PNG').convert("RGBA")
    main = image
    mark = watermark

    # Trasparenza Logo
    # mask = mark.convert('L').point(lambda x: min(x, 25))
    # mark.putalpha(mask)

    mark_width, mark_height = mark.size
    main_width, main_height = main.size
    aspect_ratio = mark_width / mark_height
    orientation = main_width / main_height

    if orientation > 1:
        basewidth = 1024
        wpercent = (basewidth / float(main.size[0]))
        hsize = int((float(main.size[1]) * float(wpercent)))
        new_mark_width = main_width * 0.25
    else:
        basewidth = 682
        wpercent = (basewidth / float(main.size[0]))
        hsize = int((float(main.size[1]) * float(wpercent)))
        new_mark_width = main_width * 0.35


    mark.thumbnail((new_mark_width, new_mark_width / aspect_ratio), Image.ANTIALIAS)
    mark_width, mark_height = mark.size
    wt_width = main_width - mark_width


    transparent = Image.new('RGB', main.size, (0,0,0,0))
    transparent.paste(main, (0,0))
    transparent.paste(mark, (wt_width,0), mask=mark)
    transparent2 = transparent.resize((basewidth,hsize), Image.ANTIALIAS)
    transparent2.save(photos_name,'PNG', dpi=[300,300])

