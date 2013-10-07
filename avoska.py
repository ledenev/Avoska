#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Alexander Ledenev"
__copyright__ = "Copyleft (>)"
__license__ = "Public Domain"
__version__ = "0.0.01"

import os
import sys
import visitors_unix

global dirs_without_read_permissions        # Change it !!! Usage of globals is not good.
dirs_without_read_permissions = []

def walk_tree(root_dir, visitor):
            # User may have no permission to access a directory to read directory contents.
            # I don't process such directories, but collect list of their names.
    try:
        names = os.listdir(root_dir)

    except PermissionError:
        dirs_without_read_permissions.append(root_dir)
        return

    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

    folders = visitor.process_folder_contents(root_dir, names)
    for entry in folders:
        full_path = os.path.join(root_dir, entry)
        walk_tree(full_path, visitor)


if __name__ == '__main__':

    root_dir = "/"

    visitor = visitors_unix.UnixDirVisitor()
    walk_tree(root_dir, visitor)
