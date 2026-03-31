import os
import subprocess
from celery import shared_task, current_task
from django.conf import settings
from .models import Video


@shared_task(bind=True)
def watermark(self, video_id):
    video = Video.objects.get(pk=video_id)
    input_path = video.video.path
    output_path = video.video_watermarks.path

    # Simuliamo progress con update_state
    try:
        self.update_state(state='PROGRESS', meta={'percent': 10, 'status': 'Preparazione input...'})
        # Eseguiamo ffmpeg con logging su stdout per leggere progress
        cmd = [
            'ffmpeg', '-y', '-loglevel', 'info', '-i', input_path,
            '-i', os.path.join(settings.STATIC_ROOT, 'images/templates/logo.png'),
            '-i', os.path.join(settings.STATIC_ROOT, 'images/templates/Codino.mp4'),
            '-filter_complex',
            '[0:v] scale=w=1280:h=720, setsar=1 [video-scaled];'
            '[1:v] scale=w=1280:h=720, setsar=1 [wm-watermarks];'
            '[2:v] scale=w=1280:h=720, setsar=1 [video2];'
            '[video-scaled][wm-watermarks]overlay=0:0 [video0];'
            '[video0][0:a][video2][2:a] concat=n=2:v=1:a=1[v][a]',
            '-map', '[v]', '-map', '[a]',
            '-crf', '18', '-preset', 'veryfast',
            '-f', 'mp4', '-strict', '-2',
            output_path
        ]
        self.update_state(state='PROGRESS', meta={'percent': 30, 'status': 'Elaborazione video...'})
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in process.stdout:
            if 'time=' in line:
                self.update_state(state='PROGRESS', meta={'percent': 60, 'status': 'Applicando filigrana...'})
        process.wait()
        self.update_state(state='PROGRESS', meta={'percent': 90, 'status': 'Finalizzazione...'})
        return {'status': 'SUCCESS', 'percent': 100}
    except Exception as exc:
        self.update_state(state='FAILURE', meta={'status': str(exc)})
        raise


        width = int(height * 16/9)
        video = Video.objects.get(id= id)
        watermark = os.path.join(settings.STATIC_ROOT) + '/images/templates/IMG_4156.PNG'
        if height == 720:
            bitrate = '4000k'
        else:
            bitrate = '10000k'

        input_file_path = video.video.path

        filename = os.path.basename(input_file_path)

        # path to the new file, change it according to where you want to put it
        output_file_name = os.path.join('video/watermarks', '{}'.format(filename))
        output_file_path = os.path.join(settings.MEDIA_ROOT, output_file_name)

        # process = FfmpegProcess(['ffmpeg', '-i', input_file_path, '-s', '{}x{}'.format(width, height), '-vcodec', 'mpeg4', '-b:v', '10000k', output_file_path])
        process = FfmpegProcess(['ffmpeg',
        '-i', input_file_path,
        '-i', watermark,
        '-filter_complex',
        '[1:v][0:v]scale2ref=({}/{})*ih/1/sar:ih/1[wm][base];[base][wm]overlay=10:10'.format(width, height),
        '-s',
        '{}:{}'.format(width, height),
        '-vcodec',
        'libx264',
        '-b:v', bitrate,
        output_file_path
        ])
        process.run(progress_handler=handle_progress_info)

        # Save the new file in the database
        video.video_720.name = output_file_name
        video.save(update_fields=['video_720'])

@shared_task
def watermark(id):
    video = Video.objects.get(id=id)
    input = video.video.path
    filename = os.path.basename(input)
    filename = os.path.splitext(filename)[0] + '.mp4'
    # SALVARE NEL DATABASE NON IL PERCORSO ASSOLUTO
    output_file_name = os.path.join('video/watermarks', '{}'.format(filename))

    # SUBPROCESS OUTPUT INVECE PERCORSO ASSOLUTO PER SALVARE
    output = os.path.join(settings.MEDIA_ROOT, output_file_name)
    codino = os.path.join(settings.STATIC_ROOT) + '/images/templates/Codino.mp4'

    width = int(video.formato)
    height = int(width/16*9)
    posizione = video.posizione
    codin = video.codino
    logo = video.logo

    if width == 1920:
        bitrate = '10000k'
    else:
        bitrate = '4000k'
    #  VIDEO ORIZZONTALE CON LOGO E CODINO
    if posizione == 'ORIZ' and codin == 'CODIN' and logo == 'LOGO':
        watermark = os.path.join(settings.STATIC_ROOT) + '/images/templates/logo.png'
        process = FfmpegProcess(['ffmpeg',
        '-y', '-loglevel', 'warning', '-i',
        input,
        '-i', watermark,
        '-i', codino,
        #'-f', 'lavfi', '-t', '0.1', '-i', 'anullsrc', #TRACCIA FITTIZIA AUDIO [3:a]
        '-filter_complex',
        '[0:v] scale=w={0}:h={1}, setsar=1 [video-scaled]; \
        [1:v] scale=w={0}:h={1}, setsar=1 [wm-watermarks]; \
        [2:v] scale=w={0}:h={1}, setsar=1 [video2]; \
        [video-scaled][wm-watermarks]overlay=0:0 [video0]; \
        [video0][0:a][video2][2:a] concat=n=2:v=1:a=1[v][a]'.format(width, height),
        '-map', '[v]',
        '-map', '[a]',
        '-crf', '18',
        '-vsync', '2',
        '-preset', 'veryfast',
        '-f', 'mp4',
        '-strict', '-2',
        output
        ])
        process.run(progress_handler=handle_progress_info)
    #  VIDEO VERTICALE CON LOGO E CODINO
    elif posizione == 'VERT' and codin == 'CODIN' and logo == 'LOGO':
        watermark = os.path.join(settings.STATIC_ROOT) + '/images/templates/logo_vertical.png'
        process = FfmpegProcess(['ffmpeg',
        '-y', '-loglevel', 'warning', '-i',
        input,
        '-i', watermark,
        '-i', codino,
        #'-f', 'lavfi', '-t', '0.1', '-i', 'anullsrc', #TRACCIA FITTIZIA AUDIO [3:a]
        '-filter_complex',
        '[0:v] split=2 [video0-1][video0-2];\
        [video0-1] scale=w={0}:h={1},boxblur=luma_radius=min(h\,w)/20:luma_power=1:chroma_radius=min(cw\,ch)/20:chroma_power=1, setsar=1 [bg0];[video0-2] scale=-1:{1}, setsar=1 [video0-2-scaled];\
        [bg0][video0-2-scaled] overlay=x=(W-w)/2:y=(H-h)/2 [video-scaled];[1:v] scale=w={0}:h={1}, setsar=1 [video-watermarks];[2:v] scale=w={0}:h={1}, setsar=1 [video2];\
        [video-scaled][video-watermarks]overlay=0:0 [video0];[video0][0:a][video2][2:a] concat=n=2:v=1:a=1[v][a]'.format(width, height),
        '-map', '[v]',
        '-map', '[a]',
        '-crf', '18',
        '-vsync', '2',
        '-preset', 'veryfast',
        '-f', 'mp4',
        '-strict', '-2',
        output
        ])
        process.run(progress_handler=handle_progress_info)
    #  VIDEO ORIZZONTALE SENZA CODINO CON LOGO
    elif posizione == 'ORIZ' and codin == 'SENZA' and logo == 'LOGO':
        watermark = os.path.join(settings.STATIC_ROOT) + '/images/templates/logo.png'
        process = FfmpegProcess(['ffmpeg',
        '-i', input,
        '-i', watermark,
        '-filter_complex',
        '[0:v] scale=w={0}:h={1}, setsar=1 [video-scaled]; \
        [1:v] scale=w={0}:h={1}, setsar=1 [wm-scaled]; \
        [video-scaled][wm-scaled]overlay=0:0'.format(width, height),
        '-crf', '18',
        '-vsync', '2',
        '-preset', 'veryfast',
        '-f', 'mp4',
        '-strict', '-2',
        output
        ])
        process.run(progress_handler=handle_progress_info)
    #  VIDEO VERTICALE SENZA CODINO CON LOGO
    elif posizione == 'VERT' and codin == 'SENZA' and logo == 'LOGO':
        watermark = os.path.join(settings.STATIC_ROOT) + '/images/templates/logo_vertical.png'
        process = FfmpegProcess(['ffmpeg',
        '-i', input,
        '-i', watermark,
        '-filter_complex',
        '[0:v] split=2 [video0-1][video0-2]; \
        [video0-1] scale=w={0}:h={1},boxblur=luma_radius=min(h\,w)/20:luma_power=1:chroma_radius=min(cw\,ch)/20:chroma_power=1, setsar=1 [bg0]; \
        [video0-2] scale=-1:{1}, setsar=1 [video0-2-scaled]; \
        [1:v] scale=w={0}:h={1}, setsar=1 [wm-scaled]; \
        [bg0][video0-2-scaled] overlay=x=(W-w)/2:y=(H-h)/2 [video-scaled]; \
        [video-scaled][wm-scaled]overlay=0:0'.format(width, height),
        '-crf', '18',
        '-vsync', '2',
        '-preset', 'veryfast',
        '-f', 'mp4',
        '-strict', '-2',
        output
        ])
        process.run(progress_handler=handle_progress_info)
    #  VIDEO ORIZZONTALE CON CODINO SENZA LOGO
    elif posizione == 'ORIZ' and codin == 'CODIN' and logo == 'SENZ':
        process = FfmpegProcess(['ffmpeg',
        '-y', '-loglevel', 'warning',
        '-i', input,
        '-i', codino,
        '-filter_complex',
        '[0:v] scale=w={0}:h={1}, setsar=1 [video-scaled]; \
        [1:v] scale=w={0}:h={1}, setsar=1 [video1]; \
        [video-scaled][0:a][video1][1:a] concat=n=2:v=1:a=1[v][a]'.format(width, height),
        '-map', '[v]',
        '-map', '[a]',
        '-crf', '18',
        '-vsync', '2',
        '-preset', 'veryfast',
        '-f', 'mp4',
        '-strict', '-2',
        output
        ])
        process.run(progress_handler=handle_progress_info)
    #  VIDEO VERTICALE CON CODINO SENZA LOGO
    elif posizione == 'VERT' and codin == 'CODIN' and logo == 'SENZ':
        process = FfmpegProcess(['ffmpeg',
        '-y', '-loglevel', 'warning', '-i',
        input,
        '-i', codino,
        '-filter_complex',
        '[0:v] split=2 [video0-1][video0-2];[video0-1] scale=w={0}:h={1},boxblur=luma_radius=min(h\,w)/20:luma_power=1:chroma_radius=min(cw\,ch)/20:chroma_power=1, setsar=1 [bg0];[video0-2] scale=-1:{1}, setsar=1 [video0-2-scaled];[bg0][video0-2-scaled] overlay=x=(W-w)/2:y=(H-h)/2 [video-scaled];[1:v] scale=w={0}:h={1}, setsar=1 [video1];[video-scaled][0:a][video1][1:a] concat=n=2:v=1:a=1[v][a]'.format(width, height),
        '-map', '[v]',
        '-map', '[a]',
        '-crf', '18',
        '-vsync', '2',
        '-preset', 'veryfast',
        '-f', 'mp4',
        '-strict', '-2',
        output
        ])
        process.run(progress_handler=handle_progress_info)
    else:
        pass


    # Save the new file in the database
    video.video_watermarks.name = output_file_name
    video.save(update_fields=['video_watermarks'])

