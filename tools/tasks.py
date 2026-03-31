import os
from pathlib import Path
from django.conf import settings
from celery import shared_task, current_task
from pytube import YouTube
from pytube.cli import on_progress


@shared_task
def video_copy(link):
        video = YouTube(link, on_progress_callback=progress_callback)

        # set video resolution
        stream = video.streams.get_lowest_resolution()
        def show_progress_bar(stream, chunk, bytes_remaining):
            size = stream.filesize
            progress = int(((size - bytes_remaining) / size) * 100)
            current_task.update_state(state='PROGRESS', meta={'current': int(progress), 'total': int(progress), 'percent': int(progress)})
            return {'current': int(progress), 'total': int(progress), 'percent': 100}
        video.register_on_progress_callback(show_progress_bar)

        # download the video
        path_yt = os.path.join(settings.MEDIA_ROOT) + '/youtube'
        os.system('rm -rf %s/*' % path_yt)
        stream.download(path_yt)


def progress_callback(stream, chunk, bytes_remaining):
    size = stream.filesize
    progress = int(((size - bytes_remaining) / size) * 100)
    return progress

