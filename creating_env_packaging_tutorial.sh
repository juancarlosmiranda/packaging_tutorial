#!/bin/bash
# Project: packaging_tutorial
#
# Github repository: https://github.com/juancarlosmiranda/packaging_tutorial
# Author: Juan Carlos Miranda
# https://juancarlosmiranda.github.io/
# https://github.com/juancarlosmiranda
#

set -e
REQUERIMENTS_LINUX='requirements_linux.txt'

# commands definitions
PYTHON_CMD='python3'
UNZIP_CMD=`which unzip`
MKDIR_CMD='mkdir -p'
CHMOD_CMD='chmod 755'
PIP_INSTALL_CMD='pip install'
PIP_UPDATE_CMD='pip install --upgrade pip'

# files extensions names
EXT_SCRIPTS_SH='*.sh'
EXT_ZIP='.zip'

# folders names definitions
COMMON_VENV_PATH='bin/activate'

# software folders names
PROJECT_NAME='packaging_tutorial'
VENV_NAME='venv'
SEPARATOR='_'

DEVELOPMENT_PATH='development'
DEVELOPMENT_ENV_PATH='development_env'

# project folders
ROOT_FOLDER_F=$HOME/$DEVELOPMENT_PATH/
PROJECT_NAME_F=$ROOT_FOLDER_F$PROJECT_NAME/
PROJECT_NAME_VENV=$PROJECT_NAME_F$SEPARATOR$VENV_EXTENSION

# environment folders
ROOT_ENV_F=$HOME/$DEVELOPMENT_ENV_PATH/
PROJECT_NAME_VENV_F=$ROOT_ENV_F$PROJECT_NAME_VENV/

# creating environments automatically
$PYTHON_CMD -m venv $PROJECT_NAME_VENV_F
source $PROJECT_NAME_VENV_F/$COMMON_VENV_PATH
$PIP_UPDATE_CMD
$PIP_INSTALL_CMD -r $PROJECT_NAME_F$REQUERIMENTS_LINUX
deactivate

