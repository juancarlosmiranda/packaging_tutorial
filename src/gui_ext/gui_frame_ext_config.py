"""
Project: Fruit Size Estimation
Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: November 2021
Description:
Manage configurations of user interface
Use:

    ui_path_config_file = os.path.join(BASE_DIR, 'conf', 'ui_frames_extractor.conf')
    ui_frame_extractor_config = GUIFrameExtractorConfig(ui_path_config_file)

"""

import os
from os.path import expanduser
import configparser


class GUIMyAppNameConfig:
    app_title = 'MY_APP_NAME_HERE v 1.0'
    width = 320
    height = 480
    geometry_about = '300x480'
    geometry_main = '600x800'
    file_extension_to_search = '.mkv'
    split_at_timestamp = 2  # time used to split files, values in seconds
    input_test_folder = ""
    user_path = None
    base_folder = None
    file_browser_input_folder = None
    file_extension_to_search = None
    input_dataset_folder = base_folder
    label_to_search = "nothing"

    def __init__(self, file_config_name=None):
        if file_config_name is not None:
            if os.path.isfile(file_config_name):
                self.f_config_name = file_config_name
                self.read_config()

    def read_config(self):
        """
        Read config from file ui_frames_extractor.conf
        :return:
        """
        f_config = configparser.ConfigParser()
        f_config.read(self.f_config_name)
        self.width = f_config['DEFAULT']['WIDTH']
        self.height = f_config['DEFAULT']['HEIGHT']
        self.geometry_about = f_config['DEFAULT']['geometry_about']
        self.geometry_main = f_config['DEFAULT']['geometry_main']
        self.user_path = f_config['DEFAULT']['user_path']
        self.base_folder = f_config['DEFAULT']['base_folder']
        self.file_browser_input_folder = f_config['DEFAULT']['file_browser_input_folder']
        self.file_extension_to_search = f_config['DEFAULT']['file_extension_to_search']
