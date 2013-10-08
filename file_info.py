#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Alexander Ledenev"
__copyright__ = "Copyleft (>)"
__license__ = "Public Domain"
__version__ = "0.0.01"

import time
import config_os_x

class FileInfo(object):
    def __init__(self, name, kind, file_mode, file_ctime, file_size):
        self.name = name
        self.attr = FileAttr(kind, file_mode, file_ctime, file_size)

    def __str__(self):
        return self.name + " : " + str(self.attr)

    def name(self):
        return self.name

    def attr(self):
        return self.attr


class FileAttr(object):
    def __init__(self, kind, file_mode, file_ctime, file_size):
        self.kind  = kind
        self.mode  = file_mode
        self.ctime = file_ctime
        self.size  = file_size

    def __str__(self):
        modif = time.strftime("%b %d, %Y %H:%M:%S", time.localtime(self.ctime))
        file_kind = config_os_x.entry_kind[self.kind]
        return "{0:s}, size = {1:d}, modif at {2:s}".format(file_kind, self.size, modif)

    def __eq__(self, other):
        if other is None:
            return False

        return \
            self.kind  == other.kind  and \
            self.mode  == other.mode  and \
            self.ctime == other.ctime and \
            self.size  == other.size
