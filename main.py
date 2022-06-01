import re
import sys
import os

from services import youtubeDownloader, twitchDownloader
from cliHelper import print_cli
from constants import YOUTUBE_REGEX, TWITCH_REGEX


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def getService(url):
    if re.search(YOUTUBE_REGEX, url):
        return youtubeDownloader
    if re.search(TWITCH_REGEX, url):
        return twitchDownloader


if __name__ == '__main__':
    if len(sys.argv) < 2:
        cls()
        print_cli('please, specify the video_url', 'error')
    else:
        getService(sys.argv[1]).download(sys.argv[1])
