#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

import os
import logging
from tkinter import filedialog
from model.directory import *
from model.file import *

logging.basicConfig(level=logging.INFO)

targetDirectory = filedialog.askdirectory()
target = directory(targetDirectory)

# dictExt={}
# for f in target.files:
#     tf = file(f)
#     logging.info(tf.ext)
#     dictExt[tf.ext] = tf.created_at

logging.info(target.sizeAll)
