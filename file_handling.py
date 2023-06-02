# ----------------------------------
# -------file handling--------------
# ----------------------------------
# 1- "a" Append   open file for appending values,create file if not exists
# 2- "r" Read     [Default value] open file for read and give error if file not exists
# 3- "w" Write    open file for writting ,create file if not exists
# 4- "x" create   create file , give error if file exists

# I have two type from paths [Absloute-Relative]


# import os  # os => operating system

# print(os.getcwd())  # cwd => current working dir   # C:\python_course\Python_course

# print(
#     os.path.dirname(os.path.abspath(__file__))
# )  # c:\python_course\Python_course=> dir for opened file

# print(
#     os.path.abspath(__file__)
# )  # c:\python_course\Python_course\file_handling.py => opened file

# # change current working dir
# os.chdir(os.path.dirname(os.path.abspath(__file__)))
# print(os.getcwd())


file = open("E:\gamal.docx")  # default mode Read and research in working directory

# file = open("E:\nfile\gamal.txt")  # through error => \n

file = open(r"E:\nfile\gamal.txt")  # r => ignore \n
