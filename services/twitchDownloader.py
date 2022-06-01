import os
from cliHelper import print_cli, draw_progress
from common import create_folder_if_not_exists
from constants import DOWNLOAD_FOLDER
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import urllib.request


def setDriver(video_url):
    op = webdriver.FirefoxOptions()
    op.add_argument('--headless')
    service = Service()
    driver = webdriver.Firefox(service=service, options=op)
    driver.set_window_position(0, 0)
    driver.set_window_size(1920, 1080)
    driver.get(video_url)
    sleep(5)
    return driver


def progress_func(block_num, block_size, total_size):
    received = block_num * block_size
    if received > total_size:
        received = total_size
    draw_progress(received, total_size)


def download(video_url):
    try:
        driver = setDriver(video_url)
        clip_url = driver.find_element(By.TAG_NAME, 'video').get_attribute('src')
        clip_title = driver.find_element(By.XPATH, "//h2[@data-a-target = 'stream-title']").text
        streamer_name = driver.find_element(By.XPATH,
                                            "/html/body/div[1]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div["
                                            "1]/div[1]/div[2]/div/div[1]/div/div[2]/div/div[2]/div[1]/div["
                                            "1]/a/h1").text
        print_cli(f'downloading video: "{streamer_name}/{clip_title}"...')
        create_folder_if_not_exists()
        urllib.request.urlretrieve(clip_url, f'{DOWNLOAD_FOLDER}/{streamer_name}_{clip_title}.mp4', progress_func)
        print_cli(f'Video successfully downloaded on '
                  f'{os.path.join(os.getcwd(), DOWNLOAD_FOLDER, streamer_name + "_" + clip_title + ".mp4")}', 'success')
    except Exception as e:
        print_cli(str(e), 'error')
