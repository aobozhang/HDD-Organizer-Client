import os
import logging
from Tkinter import *
from tkFileDialog import *
from tkMessageBox import *
from model.directory import *
from model.file import *

logging.basicConfig(level=logging.INFO)

targetDirectory = askdirectory()
target = directory(targetDirectory)

if askokcancel("Confirm!", "Press Ok to Move File in " + targetDirectory):
    target.OrganizeFiles('type');
else:
    for k, v in target.classFiles('type').items():
        logging.info (k)
        for f in v:
            logging.info (f)
