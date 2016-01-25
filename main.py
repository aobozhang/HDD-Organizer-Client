#-*- coding: UTF-8 -*-

import os,sys
import logging
from Tkinter import *
from tkFileDialog import *
from tkMessageBox import *
from model.directory import *
from model.file import *

logging.basicConfig(level=logging.INFO)

#参数1，整理方式
if len(sys.argv) >= 2 and sys.argv[1] in ['type', 'month', 'ext']:
    ogzType = sys.argv[1]
else:
    ogzType = 'type'

#参数2，目标目录
if len(sys.argv) >= 3 and os.path.exists(sys.argv[2]):
    targetDirectory = sys.argv[2]
else:
    targetDirectory = askdirectory()

target = directory(targetDirectory)

if askokcancel("Confirm!", "Press Ok to Move File in \n" + targetDirectory):
    if len(sys.argv) >= 4 and sys.argv[3] in ['-R']:
        target.OrganizeFilesAll(ogzType);
    else:
        target.OrganizeFiles(ogzType);
else:
    if len(sys.argv) >= 4 and sys.argv[3] in ['-R']:
        for k, v in target.classFilesAll(ogzType).items():
            logging.info (k)
            for f in v:
                logging.info (f)
    else:
        for k, v in target.classFiles(ogzType).items():
            logging.info (k)
            for f in v:
                logging.info (f)
