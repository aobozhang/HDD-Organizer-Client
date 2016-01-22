
import os, time
import logging
from model import file

class directory(object):

    def __init__(self, path):
        self._path   = path
        self._subDirAll = []
        self._subDir    = []
        self._filesAll  = []
        self._files     = []
        self._sizeAll   = 0
        self._size      = 0

    @property
    def path(self):
        return self._path

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

    @property
    def size(self):
        for x in self.files:
            self._size += file.file(x).size
        return self._size

    @property
    def sizeAll(self):
        for x in self.filesAll:
            self._sizeAll += file.file(x).size
        return self._sizeAll

    def classFiles(self, prop):
        d = {}
        target = self.files
        if prop == 'type':
            for f in target:
                fi = file.file(f)
                key = fi.type
                tmp = d.get(key, [])
                tmp.append(fi.path)
                d[key] = tmp
        elif prop == 'ext':
            for f in target:
                fi = file.file(f)
                key = fi.ext
                tmp = d.get(key, [])
                tmp.append(fi.path)
                d[key] = tmp
        elif prop == 'month':
            for f in target:
                fi = file.file(f)
                t = time.strftime("%Y-%m", time.localtime(fi.created_at))
                key = t
                tmp = d.get(key, [])
                tmp.append(fi.path)
                d[key] = tmp

        return d

    def classFilesAll(self, prop):
        d = {}
        target = self.filesAll
        if prop == 'type':
            for f in target:
                fi = file.file(f)
                key = fi.type
                tmp = d.get(key, [])
                tmp.append(fi.path)
                d[key] = tmp
        elif prop == 'ext':
            for f in target:
                fi = file.file(f)
                key = fi.ext
                tmp = d.get(key, [])
                tmp.append(fi.path)
                d[key] = tmp
        elif prop == 'month':
            for f in target:
                fi = file.file(f)
                t = time.strftime("%Y-%m", time.localtime(fi.created_at))
                key = t
                tmp = d.get(key, [])
                tmp.append(fi.path)
                d[key] = tmp

        return d
