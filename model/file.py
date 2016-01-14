
import os, time
import logging

class file(object):

    def __init__(self, path):
        self.path = path
        self._ext = '';
        self._created_at = '';
        self._updated_at = '';
        self._accessed_at = '';
        self._type = '';

    @property
    def ext(self):
        self._ext = os.path.splitext(self.path)[1]
        return self._ext

    @property
    def created_at(self):
        self._created_at = os.path.getctime(self.path)
        return self._created_at

    @property
    def updated_at(self):
        self._updated_at = os.path.getmtime(self.path)
        return self._updated_at

    @property
    def accessed_at(self):
        self._accessed_at = os.path.getatime(self.path)
        return self._accessed_at

    @property
    def size(self):
        self._size = os.path.getsize(self.path)
        return self._size

    @property
    def isPic(self):
        return self.ext in ['.bmp','.jpg','.jpeg','.png','.svg','.gif','.webp']

    @property
    def isOfficeDoc(self):
        return self.ext in ['.doc','.docx','.xls','.xlsx','.ppt','.pptx']

    @property
    def isVideo(self):
        return self.ext in ['.mp4','.mpg','.mpeg','.avi','.m4v','.mkv','.wmv','.asf','.flv','.mov','.m4v']

    @property
    def isAudio(self):
        return self.ext in ['.mp3','.wma','.flac','.ape','.wav','.ogg']
