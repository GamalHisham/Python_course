# ----------------------------------
# ----Modules => Built in modules---
# [1] module is a file contain a set of fun
# [2] can import module to help you
# [3] can import  Multiple module
# [4] can creat your own modules
# [5] modules save your time
# ----------------------------------

# import random  # will call all fun from module

# print(random)

# print(f"random float num {random.random()}")

# print("=" * 50)

# show all fun in module
# print(dir(random))

# print("=" * 50)

# from random import randint, random  # will call one fun from module

# print(f"random float num {random()}")

# print(f"random int {randint(10,20)}")

# ----------------------------------------------------------------------

# ----------------------------------
# ----Modules => creat own module---
# creat python file and creat fun and import it
# -----------------------------------

# import sys
# print(sys.path)  # give me a list with paths which contain modules

# call my own module
# import mymodule

# print(dir(mymodule))

# print(mymodule.sayhello("gamal"))


# Alias for module

# import mymodule as mm

# print(mm.sayhello("gamal"))

# Alias for fun in module

# from mymodule import sayhello as ss

# print(ss("gamal"))

# ---------------------------------------------------------------------

# ----Modules => install external packages---
# [1] module is a single file
# [2] package is some of modules that contain files
# [3] install package from internet with "python package manager PIP" (every language has own package manager)
# [4] PIP install package and it's Dependencies
# [5] module list : https://docs.python.org/3/py-modindex.html
# [6] packages    : https://pypi.org/
# [7] PIP manual  : https://pip.pypa.io/en/stable/cli/pip_install/
# [8] pip install package_name or module_name => to install package or module
# [9] pip list => tell me package which install in system
# [10] pip install package_name --upgrade => to update it
# [11] C:\Users\asus\AppData\Local\Programs\Python\Python311\Scripts
# -----------------------------------

import termcolor  # install it (module)
import pyfiglet  # install it (module)

# print(termcolor.colored("gamal hisham", color="red"))

# print(dir(pyfiglet)) => tell me fun in module

print(pyfiglet.figlet_format("gamal hisham"))

print(termcolor.colored(pyfiglet.figlet_format("gamal hisham"), color="red"))
