""" Module creating a window for downloading YouTube videos.
"""


import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askdirectory
from pathlib import Path
from yt_download import download_mp3, download_mp4


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
        self.download_path = str(Path.home())
        self.create_window()
    
    
    def create_window(self):
        """ Methode to call all methods that creates the different components.
        """
        self.input_field()
        self.download_format()
        self.select_folder()
        self.download()
        self.information()
    

    def  input_field(self):
        """ Create an input field where you can write down your YouTube video link.
        """
        self.input_url = tk.Entry(self, width=71, borderwidth=3, font=("Bahnschrift 16"))
        self.input_url.insert(0, "YouTube Link... (Bsp: https://www.youtube.com/...)")
        self.input_url.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


    def download_format(self):
        """ Create a LabelFrame with 2 different download formats (mp3, mp4).
        """
        self.select_format = tk.LabelFrame(self, text="Select Option", font=("Bahnschrift 16"))
        self.select_format.grid(row=1, rowspan=2, column=0, padx=10, pady=10)
        self.var_mp3 = tk.IntVar(value=1)
        self.var_mp4 = tk.IntVar()
        option_mp3 = tk.Checkbutton(self.select_format, text="mp3", variable=self.var_mp3, onvalue=1, offvalue=0, font=("Bahnschrift 16"))
        option_mp3.grid(row=0, column=0, padx=5, pady=5)
        option_mp4 = tk.Checkbutton(self.select_format, text="mp4", variable=self.var_mp4, onvalue=1, offvalue=0, font=("Bahnschrift 16"))
        option_mp4.grid(row=0, column=1, padx=5, pady=5)


    def cmd_select_folder(self):
        """ Open Explorer to choose a folder.
        """
        self.download_path = askdirectory(title="Select Folder")
        self.selected_folder_label.configure(text=self.download_path)
        
    
    def select_folder(self):
        """ Create a select-folder button with a visuel label which folder is choosen. 
        """
        self.btn_select_folder = tk.Button(self, width=20, text="Select Folder", command=self.cmd_select_folder, font=("Bahnschrift 12"), activebackground="#BDBDBD", activeforeground="red")
        self.btn_select_folder.grid(row=1, column=1)
        self.select_folder_visuel = tk.LabelFrame(self, text="Selected Folder", font=("Bahnschrift 11"))
        self.select_folder_visuel.grid(row=1, column=2, padx=10, pady=5)
        self.selected_folder_label = tk.Label(self.select_folder_visuel, text=self.download_path, font=("Bahnschrift 11"))
        self.selected_folder_label.grid(row=0, column=0)


    def cmd_download(self):
        """ Downloading youtube video.
        """
        self.info_label.configure(text="")
        success_mp3 = True
        success_mp4 = True
        if(self.var_mp3.get() == 1):  
            success_mp3 = download_mp3(self.input_url.get(), self.last_download_label, self.download_path)    
        if(self.var_mp4.get() == 1):  
            success_mp4 = download_mp4(self.input_url.get(), self.last_download_label, self.download_path)

        if success_mp3 and success_mp4:
            self.info_label.configure(text="This download has completeted!", fg="green")
        else:
            self.info_label.configure(text="There has been an error in downloading your Youtube video! Pls Check your Link!", fg="red")
    

    def download(self):
        """ Create a button and a visuel label for downloading.
        """
        self.btn_download = tk.Button(self, width=20, text="Download", command=self.cmd_download, font=("Bahnschrift 12"), activebackground="#BDBDBD", activeforeground="red")
        self.btn_download.grid(row=2, column=1)
        self.last_download_visuel = tk.LabelFrame(self, text="Last Download", font=("Bahnschrift 11"))
        self.last_download_visuel.grid(row=2, column=2, padx=10, pady=5)
        self.last_download_label = tk.Label(self.last_download_visuel, text="", font=("Bahnschrift 11"))
        self.last_download_label.grid(row=0, column=0)


    def information(self):
        """ Label for information about successful downlaod or errors.
        """
        self.info_label = tk.Label(self, text="", font=("Bahnschrift 16"))
        self.info_label.grid(row=3, column=0, columnspan=3, padx=10, pady=10)
