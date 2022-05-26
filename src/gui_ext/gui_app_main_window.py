"""
Project: Packaging Tutorial
Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: April 2022
Description:

User interface that contains functions related to MAIN SCREEN.

Use:
    ui_my_app_name_config = GUIMyAppNameConfig(ui_path_config_file)
    app = GUIMyAppWindow(ui_my_app_name_config)
    app.mainloop()
"""
import os
import tkinter as tk
from tkinter import ttk

from gui_ext.gui_app_about_window import MyAppAboutWindow
from gui_ext.gui_app_help_window import MyAppHelpWindow


class GUIMyAppWindow(tk.Tk):
    r_config = None
    dataset_config = None
    frames_extractor_config = None

    LABEL_WIDTH = 15
    ENTRY_WIDTH_PATH = 50
    BUTTON_WIDTH = 10

    tab_group = None
    tab_1 = None
    tab_2 = None
    create_dataset_frame = None
    create_dataset_options_frame = None
    user_path_label = None
    user_path_entry = None
    dataset_name_label = None
    dataset_name_entry = None
    base_path_label = None
    base_path_entry = None
    load_base_path_button = None
    create_dataset_button = None
    message_frame = None
    messages_label = None
    messages_info = None
    results_info_label = None
    results_info = None
    quit_button = None

    status_bar = None

    def __init__(self, r_config, master=None):
        super().__init__(master)
        # ---------------------------
        # configuration parameters
        self.r_config = r_config  # assign config
        # ---------------------------
        self.geometry(self.r_config.geometry_main)
        self.title(r_config.app_title)
        self.attributes('-topmost', True)
        self.state('zoomed')
        # ---------------------------
        assets_path = os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.join(assets_path, 'assets', 'icon_app.png')
        self.iconphoto(False, tk.PhotoImage(file=img_path))
        # ---------------------------
        self.create_tabs()
        self.create_widgets()
        self.create_tab_page_2()
        self.create_menu_bars()
        self.create_status_bar()
        self.create_message_info()

    def create_tabs(self):
        self.tab_group = ttk.Notebook(self)
        self.tab_1 = tk.Frame(self.tab_group)
        self.tab_2 = tk.Frame(self.tab_group)
        self.tab_group.add(self.tab_1, text='TAB_1')
        self.tab_group.add(self.tab_2, text='TAB_2')
        self.tab_group.pack(expand=1, fill="both")
        pass

    def create_tab_page_2(self):
        self.tab_2_label = tk.Label(self.tab_2, text='Label example in TAB_2:', width=self.LABEL_WIDTH)
        self.tab_2_label.grid(row=1, column=1, sticky=tk.W, ipadx=3, ipady=3)

    def create_widgets(self):
        # ############## CREATE TABS ######################
        print("create_widgets->")
        # ############## CREATE HIERARCHY ######################
        self.create_dataset_frame = tk.LabelFrame(self.tab_1, text="Create Dataset", relief=tk.RIDGE)
        self.create_dataset_frame.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        self.create_dataset_options_frame = tk.LabelFrame(self.create_dataset_frame, text="Options", relief=tk.RIDGE)
        self.create_dataset_options_frame.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        self.user_path_label = tk.Label(self.create_dataset_options_frame, text='User path:', width=self.LABEL_WIDTH)
        self.user_path_label.grid(row=1, column=1, sticky=tk.W, ipadx=3, ipady=3)

        self.user_path_entry = tk.Entry(self.create_dataset_options_frame, width=self.ENTRY_WIDTH_PATH)
        self.user_path_entry.grid(row=1, column=2, sticky=tk.W, ipadx=3, ipady=3)
        self.user_path_entry.insert(0, self.r_config.user_path)
        self.user_path_entry.config(state='readonly')

        self.dataset_name_label = tk.Label(self.create_dataset_options_frame, text='Dataset name:',
                                           width=self.LABEL_WIDTH)
        self.dataset_name_label.grid(row=2, column=1, sticky=tk.W, ipadx=3, ipady=3)

        self.base_path_label = tk.Label(self.create_dataset_options_frame, text='Base path:', width=self.LABEL_WIDTH)
        self.base_path_label.grid(row=3, column=1, sticky=tk.W, ipadx=3, ipady=3)

        self.base_path_entry = tk.Entry(self.create_dataset_options_frame, width=self.ENTRY_WIDTH_PATH)
        self.base_path_entry.grid(row=3, column=2, sticky=tk.W, ipadx=3, ipady=3)
        self.base_path_entry.insert(0, self.r_config.base_folder)
        self.base_path_entry.config(state='readonly')
        self.load_base_path_button = tk.Button(self.create_dataset_options_frame, text='Browse...',
                                               command=self.browse_base_path, width=self.BUTTON_WIDTH)
        self.load_base_path_button.grid(row=3, column=3, sticky=tk.W, ipadx=3, ipady=3)

        self.create_dataset_button = tk.Button(self.create_dataset_options_frame, text='New dataset',
                                               command=self.create_dataset_folder, width=self.BUTTON_WIDTH)
        self.create_dataset_button.grid(row=4, column=3, sticky=tk.W, ipadx=3, ipady=3)

        pass

    def create_menu_bars(self):
        """
        Add menu to the UI
        :return:
        :return:
        """
        self.menubar = tk.Menu(self)
        self.menu_file = tk.Menu(self.menubar, tearoff=False)
        self.menu_file.add_command(label="Quit", command=self.quit_app)

        self.menu_help = tk.Menu(self.menubar, tearoff=False)
        self.menu_help.add_command(label="Help...", command=self.open_help_data)
        self.menu_help.add_command(label="About...", command=self.open_about_data)

        self.menubar.add_cascade(menu=self.menu_file, label='File', underline=0)
        self.menubar.add_cascade(menu=self.menu_help, label='About', underline=0)
        self.config(menu=self.menubar)  # add menu to window

    def open_about_data(self):
        about_windows = MyAppAboutWindow(self)
        about_windows.grab_set()

    def open_help_data(self):
        help_windows = MyAppHelpWindow(self)
        help_windows.grab_set()

    def create_status_bar(self):
        print('create_status_bar->')
        self.status_bar = tk.Label(self, text="message status bar", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def create_message_info(self):
        print('create_message_info')
        ########################################################
        # MESSAGE FRAME
        self.message_frame = tk.LabelFrame(self, text="Info", relief=tk.RIDGE)
        # self.message_frame.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)
        self.message_frame.pack(expand=1, fill=tk.X)

        self.messages_label = tk.Label(self.message_frame, text='Messages:', width=self.LABEL_WIDTH)
        self.messages_label.grid(row=1, column=1, sticky=tk.W, ipadx=3, ipady=3)

        self.messages_info = tk.Text(self.message_frame, width=65, height=5)
        self.messages_info.grid(row=2, column=1, sticky=tk.W, ipadx=3, ipady=3)

        self.results_info_label = tk.Label(self.message_frame, text='Results:', width=self.LABEL_WIDTH)
        self.results_info_label.grid(row=3, column=1, sticky=tk.W, ipadx=3, ipady=3)

        self.results_info = tk.Text(self.message_frame, width=65, height=5)
        self.results_info.grid(row=4, column=1, sticky=tk.W, ipadx=3, ipady=3)

        ########################################################
        self.quit_button = tk.Button(self.message_frame, text='Quit', command=self.quit_app)
        self.quit_button.grid(row=5, column=1, sticky=tk.EW)
        ########################################################

    def not_implemented_yet(self):
        print("Not implemented yet!!!")

    def clean_text_widgets(self):
        self.messages_info.delete("1.0", "end")
        self.results_info.delete("1.0", "end")

    def browse_base_path(self):
        print('browse_base_path(self):')

    def create_dataset_folder(self):
        print('create_dataset_folder(self):')

    def browse_working_folder_data(self):
        print('browse_working_folder_data(self):')

    def select_input_folder_data(self):
        print('select_input_folder_data(self):')

    def extract_folder_data(self):
        print('extract_folder_data(self):')

    def quit_app(self):
        # ---------------------------------------------
        self.quit
        self.destroy()

# TODO: 08/04/2022 add internationalization
