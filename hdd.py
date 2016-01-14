#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

import os
import logging
from tkinter import filedialog
from model.directory import directory
logging.basicConfig(level=logging.INFO)

targetDirectory = filedialog.askdirectory()
target = directory(targetDirectory)

target.files
