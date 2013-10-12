#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Alexander Ledenev"
__copyright__ = "Copyleft (>)"
__license__ = "Public Domain"
__version__ = "0.0.01"


class FileSystemDataBase(object):
    def __init__(self):
        self.db = {}

    def read(self, dir):
        return self.db[dir]

    def write(self, dir, list):
        self.db[dir] = list


FileSystem_DB = FileSystemDataBase()
