""" Module for downloading YouTube videos in different formats.
"""


from pytube import YouTube
from pathlib import Path


def download_mp4(url, label, folder=Path.home()):
    """ Download YouTube video in mp4-format.

    Args:
        url (str): url of the YouTube video.
        label (tkinter.Label)
        folder (str, optional): Path to download directory. Defaults to Path.home().
    """
    try:
        video = YouTube(url)
        label.configure(text=video.title)
        video = video.streams.filter(file_extension='mp4').get_highest_resolution()
        video.download(folder)
        return True
    except:
        return False
    