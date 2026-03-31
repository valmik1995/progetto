import os
import shutil
import subprocess
from celery import shared_task
from django.conf import settings
from .models import Video


DEFAULT_OUTPUT_WIDTH = 1280
DEFAULT_OUTPUT_HEIGHT = 720
FFMPEG_TIMEOUT_SECONDS = 120
PROGRESS_PREP = 10
PROGRESS_PROCESSING = 30
PROGRESS_FINAL = 90
PROGRESS_DONE = 100
VERTICAL_BLUR_LUMA = 45
VERTICAL_BLUR_CHROMA = 8
CODINO_STOP_DURATION = 2
ENCODE_PRESET = 'veryfast'
ENCODE_CRF = '20'
STATUS_PREP = 'Preparazione...'
STATUS_PROCESSING = 'Elaborazione...'
STATUS_FINAL = 'Finalizzazione...'
STATUS_FALLBACK = 'Fallback completato (senza filigrana)'
STATUS_DONE = 'Completato'
FORMAT_DIMENSIONS = {
    '640': (640, 360),
    '1280': (1280, 720),
    '1920': (1920, 1080),
}


def _build_orientation_filters(is_vertical, width, height):
    if is_vertical:
        return [
            f'[0:v]scale={width}:{height},boxblur={VERTICAL_BLUR_LUMA}:{VERTICAL_BLUR_CHROMA}[bgblur]',
            f'[0:v]scale=-2:{height}:force_original_aspect_ratio=decrease,setsar=1[fgsharp]',
            '[bgblur][fgsharp]overlay=(W-w)/2:(H-h)/2[vbase]',
        ]
    return [
        f'[0:v]scale={width}:{height}:force_original_aspect_ratio=decrease,setsar=1[vscaled]',
        f'[vscaled]pad={width}:{height}:(ow-iw)/2:(oh-ih)/2:black[vbase]',
    ]


def _build_logo_filters(width, height):
    return [
        f'[1:v]scale={width}:{height},setsar=1[vwm]',
        '[vbase][vwm]overlay=0:0[vlogo]',
    ]


def _logo_file_name(is_vertical):
    return 'logo_vertical.png' if is_vertical else 'logo.png'


def _resolve_output_dimensions(formato):
    return FORMAT_DIMENSIONS.get(str(formato), (DEFAULT_OUTPUT_WIDTH, DEFAULT_OUTPUT_HEIGHT))


def _build_ffmpeg_command(input_path, output_path, is_vertical, with_logo, with_codino, output_width, output_height):
    width = output_width
    height = output_height
    cmd = ['ffmpeg', '-y', '-loglevel', 'error', '-i', input_path]
    filter_parts = _build_orientation_filters(is_vertical, width, height)
    input_idx = 1

    if with_logo:
        logo_file = _logo_file_name(is_vertical)
        logo_path = os.path.join(settings.STATIC_ROOT, f'images/templates/{logo_file}')
        cmd.extend(['-i', logo_path])
        filter_parts.extend(_build_logo_filters(width, height))
        input_idx += 1
    else:
        filter_parts.append('[vbase]null[vlogo]')

    if with_codino:
        codino_path = os.path.join(settings.STATIC_ROOT, 'images/templates/Codino.mp4')
        cmd.extend(['-i', codino_path])
        # Scala codino alle stesse dimensioni e concatena con il video principale
        filter_parts.append(f'[{input_idx}:v]scale={width}:{height}:force_original_aspect_ratio=decrease,setsar=1[vcodino]')
        filter_parts.append(f'[vlogo][vcodino]concat=n=2:v=1:a=0[vfinal]')
        # Mappa audio: prendi audio da input 0 e input codino, concatena
        filter_parts.append(f'[0:a:0][{input_idx}:a:0]concat=n=2:v=0:a=1[afinal]')
    else:
        filter_parts.append('[vlogo]null[vfinal]')

    cmd.extend([
        '-filter_complex', ';'.join(filter_parts),
        '-map', '[vfinal]',
    ])
    
    if with_codino:
        cmd.extend(['-map', '[afinal]'])
    else:
        cmd.extend(['-map', '0:a?'])
    
    cmd.extend([
        '-c:v', 'libx264',
        '-preset', ENCODE_PRESET,
        '-crf', ENCODE_CRF,
        '-c:a', 'aac',
        '-movflags', '+faststart',
        output_path,
    ])
    return cmd


def _prepare_output_paths(input_path):
    filename = os.path.basename(input_path)
    output_rel_path = os.path.join('video/watermarks', filename)
    output_path = os.path.join(settings.MEDIA_ROOT, output_rel_path)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    return output_rel_path, output_path


def _extract_video_options(video):
    return (
        video.posizione == 'VERT',
        video.logo == 'LOGO',
        video.codino == 'CODIN',
        video.formato,
    )


def _set_progress(task, percent, status):
    task.update_state(state='PROGRESS', meta={'percent': percent, 'status': status})


def _set_success(task):
    task.update_state(state='SUCCESS', meta={'percent': PROGRESS_DONE, 'status': STATUS_DONE})


def _set_failure(task, exc):
    task.update_state(state='FAILURE', meta={'status': str(exc)})


def _run_ffmpeg_with_fallback(cmd, input_path, output_path):
    try:
        subprocess.run(
            cmd,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True,
            timeout=FFMPEG_TIMEOUT_SECONDS,
            text=True,
        )
        return True
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        shutil.copy2(input_path, output_path)
        return False


def _save_video_output(video, output_rel_path):
    video.video_watermarks.name = output_rel_path
    video.save(update_fields=['video_watermarks'])


@shared_task(bind=True)
def watermark(self, video_id):
    video = Video.objects.get(pk=video_id)
    input_path = video.video.path
    is_vertical, with_logo, with_codino, formato = _extract_video_options(video)
    output_width, output_height = _resolve_output_dimensions(formato)
    output_rel_path, output_path = _prepare_output_paths(input_path)

    try:
        _set_progress(self, PROGRESS_PREP, STATUS_PREP)

        cmd = _build_ffmpeg_command(
            input_path,
            output_path,
            is_vertical,
            with_logo,
            with_codino,
            output_width,
            output_height,
        )

        _set_progress(self, PROGRESS_PROCESSING, STATUS_PROCESSING)
        ffmpeg_ok = _run_ffmpeg_with_fallback(cmd, input_path, output_path)

        final_status = STATUS_FINAL if ffmpeg_ok else STATUS_FALLBACK
        _set_progress(self, PROGRESS_FINAL, final_status)

        _save_video_output(video, output_rel_path)

        _set_success(self)
        return {'status': 'SUCCESS'}

    except Exception as exc:
        _set_failure(self, exc)
        raise
