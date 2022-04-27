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
import tkinter as tk
from gui_ext.gui_app_about_window import MyAppAboutWindow


class GUIMyAppWindow(tk.Tk):
    r_config = None
    dataset_config = None
    frames_extractor_config = None

    LABEL_WIDTH = 15
    ENTRY_WIDTH_PATH = 50
    BUTTON_WIDTH = 10

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

    def __init__(self, r_config, master=None):
        super().__init__(master)
        # ---------------------------
        # configuration parameters
        self.r_config = r_config  # assign config
        # ---------------------------
        self.geometry(self.r_config.geometry_main)
        self.title(r_config.app_title)
        self.attributes('-topmost', True)
        # ---------------------------
        self.create_widgets()
        self.create_menu_bars()

    def create_widgets(self):
        # ############## CREATE HIERARCHY ######################
        self.create_dataset_frame = tk.LabelFrame(self, text="Create Dataset", relief=tk.RIDGE)
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

        ########################################################
        # MESSAGE FRAME
        self.message_frame = tk.LabelFrame(self, text="Info", relief=tk.RIDGE)
        self.message_frame.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)

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

    def create_menu_bars(self):
        """
        Add menu to the UI
        :return:
        :return:
        """
        self.menubar = tk.Menu(self)

        # todo: delete menu option

        self.menu_file = tk.Menu(self.menubar, tearoff=False)
        self.menu_file.add_command(label="Quit", command=self.quit_app)

        self.menu_help = tk.Menu(self.menubar, tearoff=False)
        self.menu_help.add_command(label="Help...", command=self.open_about_data)
        self.menu_help.add_command(label="About...", command=self.open_about_data)

        self.menubar.add_cascade(menu=self.menu_file, label='File', underline=0)
        self.menubar.add_cascade(menu=self.menu_help, label='About', underline=0)
        self.config(menu=self.menubar)  # add menu to window

    def open_about_data(self):
        about_windows = MyAppAboutWindow(self)
        about_windows.grab_set()

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
