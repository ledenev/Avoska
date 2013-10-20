#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Alexander Ledenev"
__copyright__ = "Copyleft (>)"
__license__ = "Public Domain"
__version__ = "0.0.01"

import os
import time
from setup import config


def show_databases():
    name_filter = lambda x: config.settings['database_prefix'] == x[0:len(config.settings['database_prefix'])]

    contents = os.listdir(config.settings['database_folder'])
    list_of_databases = filter(name_filter, contents)
    return list_of_databases

def read_database(self, database_name):
    pass

def write_database(self, database_instance):
    pass

def delete_database(self, database_name):
    pass


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class CurrentDatabase(metaclass=Singleton):
    current = None
    def __init__(self):
        if self.current == None:
            database_suffix = str(time.time())
            database_name = config.settings['database_prefix'] + database_suffix
            self.current = FileSystemDatabase(database_name)

    def write(self, dir, list):
        self.current.write(dir, list)


class FileSystemDatabase(object):
    def __init__(self, name):
        self.name = name
        self.db = {}

    def read(self, dir):
        return self.db[dir]

    def write(self, dir, list):
        self.db[dir] = list
