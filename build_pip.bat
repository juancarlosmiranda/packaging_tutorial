@ echo off
REM Project: packaging_tutorial
REM
REM  Github repository: https://github.com/juancarlosmiranda/packaging_tutorial
REM  Author: Juan Carlos Miranda
REM  https://juancarlosmiranda.github.io/
REM  https://github.com/juancarlosmiranda
REM

SET PROJECT_NAME=packaging_tutorial
SET DIST_FOLDER=dist

ECHO ---------------------
ECHO CREATING PACKAGE
ECHO ---------------------
ECHO PROJECT_NAME=%PROJECT_NAME%
ECHO 'pip package is OK -- '/%DIST_FOLDER%/my_package_MY_APP_NAME_HERE-0.0.1-py3-none-any.whl
ECHO ---------------------
ECHO INSTALL PACKAGE WITH
ECHO ---------------------
ECHO 'pip install my_package_MY_APP_NAME_HERE-0.0.1-py3-none-any.whl'
py -m build