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

# open("path","mode")

# file = open("E:\gamal.docx")  # default mode Read and research in working directory

# file = open("E:\nfile\gamal.txt")  # through error => \n

# file = open(r"E:\nfile\gamal.txt")  # r => ignore \n


# -----------------------------------------------------------------------------------

# ----------------------------------
# --file handling => Read file------
# ----------------------------------

# my_file = open("C:\python_course\Python_course\gamal.txt", "r")

# print(my_file)  # file data object => name='C:\\python_course\\Python_course\\gamal.txt' mode='r' encoding='cp1256'>
# print(my_file.name)
# print(my_file.mode)
# print(my_file.encoding)


# print(my_file.read()) # read all data
# print(my_file.read(5)) # 5 => number of bytes which read from file (01 ga)

# print(my_file.readline())  # read one line
# print(my_file.read(5))  # read 5 bytes from line


# print(my_file.readlines())      # raed line and return data in list
# print(type(my_file.readlines()))


# for line in my_file:
#     print(line)

#     if line.startswith("07"):
#         break


# when finish task close file

# my_file.close()

# ------------------------------------------------------------------------------------------

# ----------------------------------
# --file handling => Write,Append---
# ----------------------------------

# my_file = open("C:\python_course\Python_course\saad.txt", "w")  # if file don't exist create it

# my_file.write("welcome\n")
# my_file.write("Hello")

# my_list = ["gamal\n", "saad\n", "emad\n"]

# my_file.writelines(my_list) # add list only


my_file = open(
    "C:\python_course\Python_course\emad.txt", "a"
)  # if file don't exist create it

my_file.write("gamal\n")
my_file.write("saad\n\n\n")
my_file.write("emad")
