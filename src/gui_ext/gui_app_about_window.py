"""
Project: Packaging Tutorial
Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: April 2022
Description:

Use:
from gui_frame_ext.about_window import AboutWindow

    def open_about_data(self):
        about_windows = MyAppAboutWindow(self)
        about_windows.grab_set()
"""
import tkinter as tk
from gui_ext.gui_frame_ext_config import GUIMyAppNameConfig


class MyAppAboutWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry(GUIMyAppNameConfig.geometry_about)
        self.title('About...')
        self.resizable(width=False, height=False)  # do not change the size
        self.attributes('-topmost', True)

        aboutLabel = tk.Label(self, text='About')
        aboutLabel.config(bg="#00ffff", font=("Verdana", 12))
        aboutLabel.pack(anchor=tk.CENTER)
        tinfo = tk.Text(self, width=40, height=5)

        about_text_info = f'MY_APP_NAME_HERE.\n' \
                          f'Juan Carlos Miranda\n' \
                          f'https://github.com/juancarlosmiranda\n' \
                          f'November 2021 \n' \
                          f'Software under development v0.1\n'

        tinfo.insert("1.0", about_text_info)
        tinfo.pack(anchor=tk.CENTER)
        buttonClose = tk.Button(self, text='Close', command=self.destroy)
        buttonClose.pack(expand=True)
