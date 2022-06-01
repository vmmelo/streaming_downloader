from pytube.exceptions import VideoUnavailable
from pytube import YouTube
from cliHelper import print_cli, draw_progress
from constants import DOWNLOAD_FOLDER

def progress_func(stream, data_chunk, bytes_remaining):
    bytes_received = stream.filesize - bytes_remaining
    draw_progress(bytes_received, stream.filesize)

def download_complete(stream, file_path):
    print_cli(f'Video successfully downloaded on {file_path}', 'success')

def download(video_url):
    try:
        yt = YouTube(video_url,
                     on_progress_callback=progress_func,
                     on_complete_callback=download_complete)

        print_cli(f'downloading video: "{yt.title}"...')
        # if yt.length > 600:
        #     raise Exception('The video needs to have less than 10 minutes length')
        yt \
            .streams \
            .filter(progressive=True, file_extension='mp4') \
            .order_by('resolution') \
            .desc() \
            .first() \
            .download(output_path=DOWNLOAD_FOLDER)
    except VideoUnavailable:
        print(f'Video {video_url} is unavaialable, skipping.')
    except Exception as e:
        print_cli(e, 'error')