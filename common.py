from constants import DOWNLOAD_FOLDER
from pathlib import Path


def create_folder_if_not_exists():
    Path(DOWNLOAD_FOLDER).mkdir(parents=True, exist_ok=True)