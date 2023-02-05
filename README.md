# README - PACKAGING TUTORIAL
This is a simple example package based on the tutorial [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
This simple application is a [Tkinter GUI based app](https://docs.python.org/es/3/library/tkinter.html)

![app_example_1](https://github.com/juancarlosmiranda/packaging_tutorial/blob/main/img/app_example_1.png?raw=true)

## Functionalities
The functionalities of the software are briefly described.
* **[Tab example]**  Tab example and Tkinter components.
* **[Icon - assets]** Example to show an icon application.
* **[Reading configurations]** Reading configurations from .conf files.
* **[PIP package building]** Using Windows to produce PIP .whl file.
* **[.EXE package building]** Using Windows + Pyinstaller to produce .EXE file.



Clone the repo or download with
```
git clone https://github.com/juancarlosmiranda/packaging_tutorial.git
```
## Install

Create a virtual environment and update environment
```
python3 -m venv ./packaging_tutorial
source ./packaging_tutorial_venv/bin/activate
py -m pip install --upgrade pip
py -m pip install --upgrade build
pip install -r requirements_linux.txt
```

Windows systems
```
%userprofile%"\AppData\Local\Programs\Python\Python38\python.exe" -m venv ./packaging_tutorial_venv
packaging_tutorial_venv\Scripts\activate.bat
pip install --upgrade pip
pip install --upgrade build
pip install -r requirements_windows.txt
```


Build package, run this command in the same directory where "pyproject.toml" is located:
```
py -m build
```

After compiling, create another virtual environment to install the files built with pip.
Copy the generated file "my_package_MY_APP_NAME_HERE-0.0.1-py3-none-any.whl" to your preferred virtual environment.
Install the new package with:

```
pip install my_package_MY_APP_NAME_HERE-0.0.1-py3-none-any.whl
```

Example
Execute application installed in another virtual environment with: 
```
python -m my_app_name
```

Upload with
```
pip install twine
twine upload ./dist/*
```
Upload for testing packages.

```
py -m twine upload --repository testpypi dist/*
```


##Documentation
```
```
##Bug Reports
```
```

##Contribution
Feel free to send pull requests. The develop branch should be used.
Please rebuild, format, check code quality and run tests before submitting a pull request:

