
import os, shutil, time
import logging

class file(object):

    def __init__(self, path):
        self._path = path

    @property
    def path(self):
        return self._path

    @property
    def ext(self):
        ori = os.path.splitext(self.path)[1]
        new = ori.replace( '.' , '' , 1)
        return new

    @property
    def created_at(self):
        return os.path.getctime(self.path)

    @property
    def updated_at(self):
        return os.path.getmtime(self.path)

    @property
    def accessed_at(self):
        return os.path.getatime(self.path)

    @property
    def size(self):
        return os.path.getsize(self.path)

    @property
    def name(self):
        return os.path.split(self.path)[1]

    @property
    def isPic(self):
        return self.ext in ['bmp','jpg','jpeg','png','svg','gif','webp']

    @property
    def isOfficeDoc(self):
        return self.ext in ['doc','docx','xls','xlsx','ppt','pptx']

    @property
    def isVideo(self):
        return self.ext in ['mp4','mpg','mpeg','avi','m4v','mkv','wmv','asf','flv','mov','m4v','rm','rmvb']

    @property
    def isAudio(self):
        return self.ext in ['mp3','wma','flac','ape','wav','ogg']

    @property
    def type(self):
        if self.isPic:
            return 'pic'
        elif self.isAudio:
            return 'audio'
        elif self.isVideo:
            return 'video'
        elif self.isOfficeDoc:
            return 'office'
        else:
            return 'other'

    def move(self, newPath):
        toExt = os.path.split(newPath)[1]
        if toExt == self.ext:
            path = newPath
        elif os.path.exists(newPath):
            path = os.path.join(newPath, self.name)
        else:
            os.mkdir(newPath)
            path = os.path.join(newPath, self.name)

        shutil.move(self.path, path)

    def rename(self, name):
        os.rename(self.name, name)
