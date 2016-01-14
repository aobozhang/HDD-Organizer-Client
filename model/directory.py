
import os
import logging
from model.file import *

class directory(object):

    def __init__(self, path):
        self.path   = path
        self._subDirAll = []
        self._subDir    = []
        self._filesAll  = []
        self._files     = []
        self._sizeAll   = 0
        self._size      = 0


    @property
    def files(self):
        for x in os.listdir(self.path):
            curPath = os.path.join(self.path, x)
            if os.path.isfile(curPath):
                self._files.append(curPath)
        return self._files

    @property
    def filesAll(self):
        for x in os.listdir(self.path):
            curPath = os.path.join(self.path, x)
            if os.path.isfile(curPath):
                self._filesAll.append(curPath)
            else:
                if os.path.isdir(curPath):
                    self._filesAll += directory(curPath).filesAll
        return self._filesAll

    @property
    def subDir(self):
        for x in os.listdir(self.path):
            curPath = os.path.join(self.path, x)
            if os.path.isdir(curPath):
                self._subDir.append(curPath)
        return self._subDir

    @property
    def subDirAll(self):
        for x in os.listdir(self.path):
            curPath = os.path.join(self.path, x)
            if os.path.isdir(curPath):
                self._subDirAll += directory(curPath).subDirAll
        return self._subDirAll

    @subDirAll.setter
    def subDirAll(self, tarList):
        self._subDirAll = tarList

    @property
    def size(self):
        for x in self.files:
            self._size += file(x).size
        return self._size

    @property
    def sizeAll(self):
        for x in self.filesAll:
            self._sizeAll += file(x).size
        return self._sizeAll
