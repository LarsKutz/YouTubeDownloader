""" Module for downloading YouTube videos in different formats.
"""


from pytube import YouTube
from pathlib import Path
import os


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
    

def download_mp3(url, label, folder=Path.home()):
    """ Download YouTube video in mp3-format.

    Args:
        url (str): url of the YouTube video.
        label (tkinter.Label)
        folder (str, optional): Path to download directory. Defaults to Path.home().
    """
    try:
        video = YouTube(url)
        label.configure(text=video.title)
        out_path = video.streams.filter(only_audio=True).first().download(folder)
        new_name = os.path.splitext(out_path)
        if(os.path.exists(new_name[0] + '.mp3')):
            os.remove(new_name[0] + '.mp3')
        os.rename(out_path, new_name[0] + '.mp3') 
        return True
    except:
        return False
