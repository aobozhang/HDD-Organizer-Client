
import os
import logging

class directory(object):

    def __init__(self, path):
        self.path   = path
        self._subDirAll = []
        self._subDir    = []
        self._files     = []

    @property
    def files(self):
        for x in os.listdir(self.path):
            curPath = os.path.join(self.path, x)
            if os.path.isfile(curPath):
                logging.info(curPath)
                self._files.append(curPath)
        return self._files

    @property
    def subDir(self):
        for x in os.listdir(self.path):
            curPath = os.path.join(self.path, x)
            if os.path.isdir(curPath):
                logging.info(curPath)
                self._subDir.append(curPath)
        return self._subDir

    @property
    def subDirAll(self):
        for x in os.listdir(self.path):
            curPath = os.path.join(self.path, x)
            if os.path.isdir(curPath):
                logging.info(curPath)
                self._subDirAll += directory(curPath).subDirAll
        return self._subDirAll

    @subDirAll.setter
    def subDirAll(self, tarList):
        self._subDirAll = tarList
