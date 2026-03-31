from __future__ import absolute_import, unicode_literals
import os
import re
import time
import subprocess
import random
from datetime import timedelta
from django.utils import timezone
from PIL import Image, ImageDraw, ImageFont
from celery import shared_task, current_task
from time import sleep
from zipfile import ZipFile
from django.conf import settings
from foto.models import *
import os
import PIL

@shared_task
def add(x, y):
    return x + y

@shared_task
def increment(Limit, wait_time=0.5):
    for cnt in range(Limit):
        current_task.update_state(
                state="PROGRESS",
                meta={
                    'iteration': cnt,
                    'status': 'INCREMENTING...',
                    }
                )
        print ("Counter: {}".format(cnt))
        time.sleep(wait_time)

@shared_task
def photo_watermark(total):
    for id in total:
        files = Photo.objects.get(id=id)
        input_file_path = files.file.path
        filename = os.path.basename(input_file_path)
        filename = os.path.splitext(filename)[0] + '.jpeg'

        output_file_name = os.path.join('watermarks', '{}'.format(filename))
        final_image_path = os.path.join(settings.MEDIA_ROOT, output_file_name)
        watermark = os.path.join(settings.STATIC_ROOT) + '/images/templates/IMG_4156.PNG'


        main = Image.open(input_file_path)
        mark = Image.open(watermark)

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
        transparent2.save(final_image_path, "JPEG", quality=100,
                          optimize=True, progressive=True)

        # Save the new file in the database
        Photo.objects.filter(id=id).update(file_watermark=output_file_name)
        new_list = [i for i in range(1,len(total)+1)]
        totale = new_list[-1]
        new_dict = dict(zip(total, new_list))
        current_task.update_state(state='PROGRESS',meta={'current': new_dict[id], 'total': totale, 'percent': int((float(new_dict[id]) / totale) * 100)})
    return {'current': totale, 'total': totale, 'percent': 100}

@shared_task(bind=True)
def photo_watermark_heic(self):
    path = PhotoHeic.objects.all()
    watermark = os.path.join(settings.STATIC_ROOT) + '/images/templates/IMG_4156.PNG'
    for star in path.iterator():
        input_file_path = star.file.path
        input_file_name = star.file.name
        filename = os.path.basename(input_file_path)

        output_file_name = os.path.join('heic/jpeg', '{}'.format(filename))
        output_file_path = os.path.join(settings.MEDIA_ROOT, output_file_name)
        output_file_path = os.path.splitext(output_file_path)[0]+'.jpeg'
        # subprocess.call(['/usr/local/bin/ffmpeg', '-i', input_file_path, '-s', '{}x{}'.format(width, height), '-vcodec', 'mpeg4', '-b:v', '10000k', output_file_path])
        subprocess.call(['convert',
        input_file_path,
        '-resize',
        '1024',
        '-density',
        '96',
        output_file_path
        ])
        file_path = os.path.splitext(output_file_name)[0]+'.jpeg'
        # Save the new file in the database
        change = PhotoHeic.objects.get(id = star.id)
        change.file_heic = file_path
        change.save()

@shared_task(bind=True)
def make_thumbnails(file_path, thumbnails=[]):
    os.chdir(settings.IMAGES_DIR)
    path, file = os.path.split(file_path)
    file_name, ext = os.path.splitext(file)

    zip_file = f"{file_name}.zip"
    results = {'archive_path': f"{settings.MEDIA_URL}images/{zip_file}"}
    try:
        img = Image.open(file_path)
        zipper = ZipFile(zip_file, 'w')
        zipper.write(file)
        os.remove(file_path)
        for w, h in thumbnails:
            img_copy = img.copy()
            img_copy.thumbnail((w, h))
            thumbnail_file = f'{file_name}_{w}x{h}.{ext}'
            img_copy.save(thumbnail_file)
            zipper.write(thumbnail_file)
            os.remove(thumbnail_file)

        img.close()
        zipper.close()
    except IOError as e:
        print(e)

    return results

@shared_task
def save_image_to_models():
    results = Galleria.objects.all()
    for result in results:
        print(result.id)

@shared_task
def watermarks(total):
    for id in total:
        files = Galleria.objects.get(id=id)
        input_file_path = files.image.path
        filename = os.path.basename(input_file_path)
        ext = filename.split('.')[-1]
        title = re.sub(r"[^a-zA-Z0-9]", "_", files.title).lower()
        new_filename = title + "_" + str(id) + ".jpg"



        #INIZIO WATERMARKS
        output_file_name_wt = os.path.join(
            'galleria/watermarks', '{}'.format(new_filename))
        final_image_path_wt = os.path.join(settings.MEDIA_ROOT, output_file_name_wt)
        watermark = os.path.join(settings.STATIC_ROOT) + '/images/templates/IMG_4156.PNG'

        main = Image.open(input_file_path)
        mark = Image.open(watermark)

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
        transparent2.save(final_image_path_wt, 'JPEG', quality=100)

        #INIZIO THUMBAILS
        rename = title + "_" + str(id) + '.jpg'
        output_file_name_th = os.path.join('galleria/thumbails', '{}'.format(rename.lower()))
        output_file_path = os.path.join(settings.MEDIA_ROOT, output_file_name_th)
        arial = os.path.join(settings.STATIC_ROOT) + "/fonts/arial/arial.ttf"
        img = Image.open(input_file_path).convert("RGBA")
        fixed_height = 1024
        height_percent = (fixed_height / float(img.size[1]))
        width_size = int((float(img.size[0]) * float(height_percent)))
        img = img.resize((width_size, fixed_height), PIL.Image.NEAREST)
        txt = Image.new('RGBA', img.size, (255, 255, 255, 0))
        #Opening Image & Creating New Text Layerimg = Image.open(input_file_path).convert('RGBA')txt = Image.new('RGBA', img.size, (255,255,255,0))
        #Opening Image & Creating New Text Layer

        #Creating Text
        text = "@vigilfuoco.tv"
        font = ImageFont.truetype(arial, 50)

        #Creating Draw Object
        draw = ImageDraw.Draw(txt)

        #Positioning of Text
        width, height = img.size
        # textwidth, textheight = d.textsize(text, font)
        # x=width/2-textwidth/2

        # Loop for Multiple Watermarks
        y = 10
        for i in range(10):
            x = random.randint(0, width)
            y += random.randrange(0, int(height/8), 10)+random.randint(0, 30)
            draw.text((x, y), text, fill=(255, 255, 255, 75), font=font)

        #Combining both layers and saving new image
        watermarked = Image.alpha_composite(img, txt)
        watermarked = watermarked.convert('RGB')
        #Combining both layers and saving new image
        watermarked.save(output_file_path, optimize=True, quality=70)

        #RINOMINA FILES ORIGINALE
        initial_path = os.path.join(settings.MEDIA_ROOT, input_file_path)
        new_orginale_filename = title + "_" + str(id) + "." + ext
        new_originale_image_database = "galleria/originale/" + new_orginale_filename
        new_originale_path = os.path.join(
            settings.MEDIA_ROOT, new_originale_image_database)
        os.rename(initial_path, new_originale_path)

        # Save the new file in the database
        Galleria.objects.filter(id=id).update(image=new_originale_image_database,
                                          image_thumbails=output_file_name_th, image_watermarks=output_file_name_wt)
        new_list = [i for i in range(1,len(total)+1)]
        totale = new_list[-1]
        new_dict = dict(zip(total, new_list))
        current_task.update_state(state='PROGRESS',meta={'current': new_dict[id], 'total': totale, 'percent': int((float(new_dict[id]) / totale) * 100)})
    return {'current': totale, 'total': totale, 'percent': 100}

@shared_task
def make_thumbnails(file_path, thumbnails=[]):
    os.chdir(settings.IMAGES_DIR)
    path, file = os.path.split(file_path)
    file_name, ext = os.path.splitext(file)

    zip_file = f"{file_name}.zip"
    results = {'archive_path': f"{settings.MEDIA_URL}images/{zip_file}"}
    try:
        img = Image.open(file_path)
        zipper = ZipFile(zip_file, 'w')
        zipper.write(file)
        os.remove(file_path)
        for w, h in thumbnails:
            img_copy = img.copy()
            img_copy.thumbnail((w, h))
            thumbnail_file = f'{file_name}_{w}x{h}.{ext}'
            img_copy.save(thumbnail_file)
            zipper.write(thumbnail_file)
            os.remove(thumbnail_file)

        img.close()
        zipper.close()
    except IOError as e:
        print(e)

    return results

    
