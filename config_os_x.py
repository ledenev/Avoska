#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Alexander Ledenev"
__copyright__ = "Copyleft (>)"
__license__ = "Public Domain"
__version__ = "0.0.01"


path_to_database = "/Volumes/files-hdd/Avoska_DB"

root_system_names = (
    ".DocumentRevisions-V100",
    ".Spotlight-V100",
    ".Trashes",
    ".file",
    ".fseventsd",
    ".vol",
    "Network",
    "Volumes",
    "cores",
    "dev",
    "etc",
    "mach_kernel",
    "net",
    "private",
    "tmp",
    "var"
)

system_names = (
    ".localized",
    ".DS_Store",
    ".Trash"
)

error_id  = 0
file_id   = 1
link_id   = 2
folder_id = 3

entry_kind = ("error ", "file  ", "link  ", "folder")
