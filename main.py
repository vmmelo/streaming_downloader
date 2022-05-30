from pytube import YouTube
import sys


def download_yt_video(video_url):
    try:
        print('validating video url')
        yt = YouTube(video_url)
        print(yt.title)
        if yt.length > 600:
            raise Exception('The video needs to have less than 10 minutes length')
        yt\
            .streams\
            .filter(progressive=True, file_extension='mp4')\
            .order_by('resolution')\
            .desc()\
            .first()\
            .download(output_path=f'outputs/')
    except Exception as e:
        print(str(e))
    else:
        print("Video downloaded successfully")


if __name__ == '__main__':
    print(sys.argv, len(sys.argv))
    if len(sys.argv) < 2:
        print('please specify the video_url argument')
    download_yt_video(sys.argv[1])
