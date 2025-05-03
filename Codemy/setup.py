'''
# setup.py for packaging a PyQt5 application using py2app
'''
from setuptools import setup

APP = ['ToDo_icon.py']  # Your main script
DATA_FILES = []    # Include any data files or assets here
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'rubberDuckey.icns',
    'packages': ['PyQt5'],  # Add other needed packages here
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
# This setup script is for packaging a PyQt5 application using py2app.