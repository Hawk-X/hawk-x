#!/usr/bin/python

import os
import shutil

try:
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)))
    os.remove("src/dev.sqlite")
    shutil.rmtree(
        "src/.idea",
        "src/.sass-cache",
        "src/hawk/__pycache__",
        "src/prox/__pycache__",
        "src/prox/migrations",
        "src/shop/__pycache__",
        "src/shop/migrations"
    )
    print("\033[1;31mDONE!  \033[1;m")
except:
    print("Already delete. No such file or directory.")
    raise OSError
