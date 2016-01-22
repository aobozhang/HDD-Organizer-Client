import os
import logging
from tkinter import filedialog
from model.directory import *
from model.file import *

logging.basicConfig(level=logging.INFO)

targetDirectory = filedialog.askdirectory()

logging.info('# Path : ', targetDirectory)

target = directory(targetDirectory)
for k, v in target.classFilesAll('type').items():
    logging.info (k)
    for f in v:
        logging.info (f)
