#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Alexander Ledenev"
__copyright__ = "Copyleft (>)"
__license__ = "Public Domain"
__version__ = "0.0.01"

import os
import sys
import visitors_unix
import filesystem_db
from setup import config

global dirs_without_read_permissions       # Change it !!! Usage of globals is not good.


def walk_tree(directory, visitor):
            # User may have no permission to access a directory to read directory contents.
            # I don't process such directories, but collect list of their names.
    try:
        names = os.listdir(directory)

    except PermissionError:
        dirs_without_read_permissions.append(directory)
        return

    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

    folders = visitor.process_directory_contents(directory, names)
    for entry in folders:
        full_path = os.path.join(directory, entry)
        walk_tree(full_path, visitor)


if __name__ == '__main__':
    dirs_without_read_permissions = []

    root_dir = config.settings["root_dir"]
    visitor = visitors_unix.UnixDirVisitor()
    walk_tree(root_dir, visitor)
    db = filesystem_db.CurrentDatabase()
    db.save()

#----------   Test: print latest database   ----------
    databases = filesystem_db.show_databases()
    db_tst = filesystem_db.CurrentDatabase(databases[-1])
    db_tst.print_db()
