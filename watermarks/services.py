import os
from io import BytesIO

from django.conf import settings
from django.core.files.base import ContentFile
from PIL import Image

from watermarks.models import Photo

try:
    from pillow_heif import register_heif_opener

    register_heif_opener()
except Exception:
    register_heif_opener = None


def _watermark_asset_path():
    candidate_paths = [
        os.path.join(settings.STATIC_ROOT, 'images', 'templates', 'IMG_4156.PNG'),
        os.path.join(settings.BASE_DIR, 'static', 'images', 'templates', 'IMG_4156.PNG'),
    ]
    for path in candidate_paths:
        if path and os.path.exists(path):
            return path
    raise FileNotFoundError('Watermark asset IMG_4156.PNG non trovato.')


def _apply_watermark(source_image: Image.Image) -> Image.Image:
    watermark_image = Image.open(_watermark_asset_path()).convert('RGBA')
    main = source_image.convert('RGBA')

    main_width, main_height = main.size
    orientation = main_width / main_height

    if orientation > 1:
        base_width = 1024
        mark_ratio = 0.25
    else:
        base_width = 682
        mark_ratio = 0.35

    wpercent = base_width / float(main_width)
    hsize = int(float(main_height) * float(wpercent))
    resized_main = main.resize((base_width, hsize), Image.LANCZOS)

    new_mark_width = int(resized_main.size[0] * mark_ratio)

    mark_width, mark_height = watermark_image.size
    aspect_ratio = mark_width / mark_height
    watermark_image.thumbnail((new_mark_width, new_mark_width / aspect_ratio), Image.LANCZOS)

    resized_mark_width, _ = watermark_image.size
    paste_x = resized_main.size[0] - resized_mark_width

    canvas = Image.new('RGBA', resized_main.size, (0, 0, 0, 0))
    canvas.paste(resized_main, (0, 0))
    canvas.paste(watermark_image, (paste_x, 0), mask=watermark_image)
    return canvas


def create_photo_with_watermark(uploaded_file):
    photo = Photo.objects.create(file=uploaded_file)

    source_path = photo.file.path
    original_name = os.path.basename(photo.file.name)
    base_name, ext = os.path.splitext(original_name)
    ext = ext.lower()

    if ext in {'.heic', '.heif'} and register_heif_opener is None:
        raise RuntimeError('Supporto HEIC/HEIF non disponibile: installa pillow-heif.')

    with Image.open(source_path) as source_image:
        output_image = _apply_watermark(source_image)

    output_buffer = BytesIO()
    if ext == '.png':
        output_ext = '.png'
        output_image.save(output_buffer, format='PNG', optimize=True)
    else:
        output_ext = '.jpeg'
        output_image.convert('RGB').save(
            output_buffer,
            format='JPEG',
            quality=95,
            optimize=True,
            progressive=True,
        )

    output_rel_path = f"{base_name}{output_ext}"
    photo.file_watermark.save(output_rel_path, ContentFile(output_buffer.getvalue()), save=False)
    photo.save(update_fields=['file_watermark'])
    return photo
