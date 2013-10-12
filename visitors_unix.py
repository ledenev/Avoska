#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Alexander Ledenev"
__copyright__ = "Copyleft (>)"
__license__ = "Public Domain"
__version__ = "0.0.01"

import os
import file_info
import filesystem_db
from setup import config_os_x


class UnixDirVisitor(object):

    def process_directory_contents(self, dir_name, names):
        folders = []
        file_info_list = []
        names = self.filter_out_system_names(dir_name, names)

        for entry in names:
            full_name = os.path.join(dir_name, entry)

            if os.path.islink(full_name):
                entry_id = config_os_x.link_id
            elif os.path.isfile(full_name):
                entry_id = config_os_x.file_id
            elif os.path.isdir(full_name):
                folders.append(entry)
                entry_id = config_os_x.folder_id
            else:
                print("Error: %s - wrong kind of file name !!!" % entry)
                exit(1)

            stat_info = os.lstat(full_name)
            info = file_info.FileInfo(entry, entry_id, stat_info.st_mode, stat_info.st_ctime, stat_info.st_size)
            file_info_list.append(info)

        filesystem_db.FileSystem_DB.write(dir_name, file_info_list)

        return folders


    def filter_out_system_names(self, dir_name, names):
        new_names = [entry for entry in names if not entry in config_os_x.system_names]
        if dir_name == "/":
            new_names = [entry for entry in new_names if not entry in config_os_x.root_system_names]

        return new_names
