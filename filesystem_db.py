#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Alexander Ledenev"
__copyright__ = "Copyleft (>)"
__license__ = "Public Domain"
__version__ = "0.0.01"

import os
from setup import config

class DatabaseManager(object):
    def show_databases(self):
        name_filter = lambda x: config.settings['database_prefix'] == x[0:len(config.settings['database_prefix'])]

        contents = os.listdir(config.settings['database_folder'])
        database_list = filter(name_filter, contents)
        return database_list

    def write_database(self, database_instance):
        pass

    def read_database(self, database_name):
        pass

    def delete_database(self, database_name):
        pass


class FileSystemDatabase(object):
    def __init__(self):
        self.db = {}

    def read(self, dir):
        return self.db[dir]

    def write(self, dir, list):
        self.db[dir] = list


FileSystem_DB = FileSystemDatabase()
