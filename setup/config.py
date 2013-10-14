#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Alexander Ledenev"
__copyright__ = "Copyleft (>)"
__license__ = "Public Domain"
__version__ = "0.0.01"

import os

path_to_database = os.path.expanduser("~/Avoska_DB")

settings = dict(
    root_dir = "/",
    database_folder = path_to_database,
    database_prefix = "filesystem_")

try:
    from setup import local

    for key in local.settings.keys():
        settings[key] = local.settings[key]

except ImportError:
    pass
