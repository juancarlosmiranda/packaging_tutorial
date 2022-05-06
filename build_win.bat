@ echo off
SET APPLICATION_NAME=
SET APPLICATION_PATH=%~dp0

SET CONF_NAME=*.conf
SET PAHT_FOLDER_RELATIVE=src\my_app_name\conf\
SET PATH_CONF_FILE=%APPLICATION_PATH%%PAHT_FOLDER_RELATIVE%%CONF_NAME%


SET DESTINATION_FOLDER_RELATIVE=dist\package_tutorial\conf
SET DESTINATION_FOLDER_ABSOLUTE=%APPLICATION_PATH%%DESTINATION_FOLDER_RELATIVE%


ECHO %APPLICATION_PATH%
ECHO %PATH_CONF_FILE%
ECHO %DESTINATION_FOLDER_ABSOLUTE%

REM uncomment the following line if you need to generate again __main__.spec
REM pyi-makespec --paths=%APPLICATION_PATH%src\my_app_name --paths=%APPLICATION_PATH%src\gui_ext --paths=%APPLICATION_PATH%src\helpers %APPLICATION_PATH%src\my_app_name\__main__.py
pyinstaller win_exe_conf/__main__.spec ./src/my_app_name/__main__.py -y


REM copy .conf files to executable
MKDIR %DESTINATION_FOLDER_ABSOLUTE%
COPY %PATH_CONF_FILE% %DESTINATION_FOLDER_ABSOLUTE%