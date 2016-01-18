#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

import os
import logging
from tkinter import filedialog
from model.directory import *
from model.file import *
from view.main import *

logging.basicConfig(level=logging.INFO)

targetDirectory = filedialog.askdirectory()
target = directory(targetDirectory)

logging.info(target.classFilesAll('month'))


# app = main()
# # 设置窗口标题:
# app.master.title('Hello World')
# # 主消息循环:
# app.mainloop()
