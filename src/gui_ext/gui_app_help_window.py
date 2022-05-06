"""
Project: Packaging Tutorial
Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: April 2022
Description:

Use:
from gui_frame_ext.help_window import MyAppHelpWindow

    def open_about_data(self):
        help_windows = MyAppHelpWindow(self)
        help_windows.grab_set()
"""
import os
import tkinter as tk
from gui_ext.gui_frame_ext_config import GUIMyAppNameConfig


class MyAppHelpWindow(tk.Toplevel):
    author_str = 'Juan Carlos Miranda'
    author_site_str = 'https://github.com/juancarlosmiranda'
    title_str = 'MY_APP_NAME_HERE'
    version_number_str = '1.0'
    release_date = 'April 2022'

    def __init__(self, parent):
        super().__init__(parent)
        self.geometry(GUIMyAppNameConfig.geometry_about)
        self.title('HELP...')
        self.resizable(width=False, height=False)  # do not change the size
        self.attributes('-topmost', True)
        assets_path = os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.join(assets_path, 'assets', 'icon_app.png')
        self.iconphoto(False, tk.PhotoImage(file=img_path))

        about_label = tk.Label(self, text=self.title_str)
        about_label.config(font=("Verdana", 12))
        about_label.pack(anchor=tk.CENTER)
        text_info = tk.Label(self)
        help_text_info = f'HELP WINDOW\n' \
                          f'Software under development {self.version_number_str}\n'

        text_info['text'] = help_text_info
        text_info.pack(anchor=tk.CENTER)

        img_label = tk.Label(self)
        #assets_path = os.path.dirname(os.path.abspath(__file__))
        #img_path = os.path.join(assets_path, 'assets', 'logo_help.png')
        #img_label.image = tk.PhotoImage(file=img_path)
        #img_label['image'] = img_label.image
        #img_label.pack()

        buttonClose = tk.Button(self, text='Close', command=self.destroy)
        buttonClose.pack(expand=True)
