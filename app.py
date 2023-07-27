""" Module creating a window for downloading YouTube videos.
"""


import tkinter as tk
from PIL import Image, ImageTk


class App(tk.Tk):
    """ Class for creating a window for downloading YouTube videos in different formats.

    Extends:
        tk (class.Tk): Extends Class Tk as base-class.
    """
    def __init__(self):
        """ Constructor
        """
        super().__init__()
        
        self.WIDTH = 1920
        self.HEIGHT = 1080
        self.title("YouTube Downloader")
        self.maxsize(self.WIDTH, self.HEIGHT)
        self.resizable(False, False)
        self.ICON = ImageTk.PhotoImage(Image.open('icons/youtube_256x256.ico'))
        self.wm_iconphoto(False, self.ICON)
        self.create_window()
    
    
    def create_window(self):
        """ Methode to call all methods that creates the different components.
        """
        pass
    