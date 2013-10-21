#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Alexander Ledenev"
__copyright__ = "Copyleft (>)"
__license__ = "Public Domain"
__version__ = "0.0.01"

import os
import time
import pickle
from setup import config

#==========   Database Record   ==========

class DatabaseRecord(object):

    def __init__(self, directory):
        self.dir_name = directory
        self.entries_list = []

    def __str__(self):
        contents_str = ','.join([str(x) for x in self.entries_list])
        return self.dir_name + " : " + contents_str

    def directory(self):
        return self.dir_name

    def contents(self):
        return self.entries_list

    def set_contents(self, entries):
        self.entries_list = entries

    def append(self, entry):
        self.entries_list.append(entry)

    def compare(self, other):
        '''
        Current object is current record
        The argument 'other' is older record
        Returns tuple: (list of deleted entries, list of new entries)
        '''
        if other is None:
            print("Error: Argument of compare is None")
            exit(1)

        if self.dir_name != other.directory():
            print("Error: Names of directories for comparison are not the same")
            exit(1)

        if other == [] or self.contents == []:
            return (other, self.contents)
        else:
            old_set = set(other)
            current_set = set(self.contents)
            return (list(old_set - current_set), list(current_set - old_set))


#==========   Database   ==========

class FileSystemDatabase(object):

    def __init__(self, database_name = ""):
        if database_name == "":
            self.db_name = config.settings['db_name_prefix'] + str(time.time())
            self.db = {}
        else:
            self.load(database_name)

    def __str__(self):
        return self.db_name

    def name(self):
        return self.db_name

    def version(self):
        db_prefix, db_version = self.db_name.split(config.settings['db_name_prefix_end'])
        return float(db_version)

    def version_str(self):
        return time.strftime("%d %b %Y %H:%M:%S", self.version())

    def read(self, dir):
        record = DatabaseRecord(dir)
        record.set_contents(self.db[dir])
        return record

    def write(self, db_record):
        dir = db_record.directory()
        self.db[dir] = db_record.contents()

    def load(self, database_name):
        self.db_name = database_name
        db_full_name = os.path.join(config.settings['database_folder'], database_name)
        try:
            db_file = open(db_full_name, 'rb')
            self.db = pickle.load(db_file)
            db_file.close()
        except FileNotFoundError:
            print("No such file or directory: %s" % db_full_name)
            exit(1)

    def save(self):
        db_full_name = os.path.join(config.settings['database_folder'], self.db_name)
        try:
            db_file = open(db_full_name, 'wb')
            pickle.dump(self.db, db_file)
            db_file.close()
        except:
            print("Error: database save ")
            exit(1)

    def print_db(self):
        db_full_name = os.path.join(config.settings['database_folder'], self.db_name)
        print()
        print("        Database: %s" % db_full_name)

        for dir in self.db:
            print()
            print(dir)
            for file_inf in self.db[dir]:
                print("    %s" % str(file_inf))


#==========   Current Database Singleton   ==========

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class CurrentDatabase(FileSystemDatabase, metaclass=Singleton):
    def __init__(self):
        super().__init__()


#==========   Operations with Databases   ==========

def show_databases():
    prefix_length = len(config.settings['db_name_prefix'])
    contents = os.listdir(config.settings['database_folder'])
    list_of_databases = [name for name in contents if name[:prefix_length] == config.settings['db_name_prefix']]
    return list_of_databases

def delete_database(database_name):
    os.remove(os.path.join(config.settings['database_folder'], database_name))
