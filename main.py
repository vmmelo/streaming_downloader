from pytube import YouTube
import sys
import os

from pytube.exceptions import VideoUnavailable

DOWNLOAD_FOLDER = 'yt_downloader'


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def progress_func(stream, data_chunk, bytes_remaining):
    print(stream.filesize)
    print(bytes_remaining)


def download_complete(stream, file_path):
    print_cli(f'Video downloaded successfully on {file_path}', 'success')


def download_yt_video(video_url):
    try:
        yt = YouTube(video_url,
                     on_progress_callback=progress_func,
                     on_complete_callback=download_complete)

        print_cli(f'downloading video: "{yt.title}"...')
        if yt.length > 600:
            raise Exception('The video needs to have less than 10 minutes length')
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


def print_cli(text, message_type=''):
    r = 255
    g = 255
    b = 255
    if message_type == 'error':
        g = 0
        b = 0
    elif message_type == 'success':
        r = 0
        b = 0
    return print("\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        cls()
        print_cli('please, specify the video_url argument', 'error')
    else:
        download_yt_video(sys.argv[1])
