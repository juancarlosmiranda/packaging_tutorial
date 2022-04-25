from os.path import expanduser
from gui_ext.gui_frame_ext_config import GUIMyAppNameConfig
from gui_ext.gui_app_main_window import GUIMyAppWindow
from helpers.helper_filesystem import *

if __name__ == '__main__':
    BASE_DIR = os.path.abspath('.')
    path_user_config_files = os.path.join(BASE_DIR, 'conf')
    ui_path_config_file = os.path.join(BASE_DIR, 'conf', 'my_app_config.conf')
    user_path = expanduser("~")
    current_main_path_str = __file__
    package_path = os.path.dirname(os.path.normpath(current_main_path_str))
    package_path_config_files = os.path.join(package_path, 'conf')

    print('BASE_DIR->', BASE_DIR)
    print('user_path->', user_path)
    print('saved_str', current_main_path_str)
    print('package_path', package_path)
    print('ui_path_config_file->', ui_path_config_file)
    print('path_user_config_files->', path_user_config_files)

    # if directory doen't exist, then create
    if os.path.exists(path_user_config_files):
        print('Directory exist!!!', path_user_config_files)
    else:
        print('Directory doesnt exist!!!', path_user_config_files)
        print('Creating directory ', path_user_config_files)
        os.mkdir(path_user_config_files)
        copy_folder(package_path_config_files, path_user_config_files)

    # -------------------------
    ui_my_app_name_config = GUIMyAppNameConfig(ui_path_config_file)
    app = GUIMyAppWindow(ui_my_app_name_config)
    app.mainloop()
    # -------------------------