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
        self.input_field()
    

    def  input_field(self):
        """ Create an input field where you can write down your YouTube video link.
        """
        self.input_url = tk.Entry(self, width=71, borderwidth=3, font=("Bahnschrift 16"))
        self.input_url.insert(0, "YouTube Link... (Bsp: https://www.youtube.com/...)")
        self.input_url.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
