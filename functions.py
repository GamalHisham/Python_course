# ______________________________
# ___________Functions__________
# 1- A function is a block of code do a task
# 2- A function run when you call it
# 3- A function accept element to deal with called [parameters]
# 4- A function can do task without returning data
# 5- A function can return data after JOb is finished
# 6- A function creat to prevent dry
# 7- A function accept element when you call it  called [Arguments]
# 8- There's a built_in functions and user defined functions
# 9- A function is all for team and all apps
# ______________________________


# def print_name (): #A function can do task without returning data

#     print("gamal hisham saad")

# print_name()


# def print_name (): #A function can return data after JOb is finished

#     name = "gamal hisham saad"
#     return name

# print(print_name())

# -----------------------------------------------------------------------------------------------

# ______________________________
# ____parameters and arguments__
# _______________________________

# def                            => function keyword
# say_hello                      => function name
# name                           => function parameter
# print(f"hello {name}")         => function task
# say_hello("gamal")             => gamal is  argument


# def say_hello (name):

#     print(f"hello {name}")


# say_hello("gamal")

# -----------------------------------------------------------

# def addition (n1,n2):

#     if type(n1) != int or type(n2) != int :
#         print ("only add integers numbers")

#     else:
#         print(n1+n2)

# addition(100,300)

# addition("100",300)

# ---------------------------------------------------------------


# def full_name(f, m, l):
#     print(f" hello {f.strip().capitalize()} {m.upper():.1s} {l.capitalize()}")


# full_name("  gamal   ","hisham" ,"saad")

# -------------------------------------------------------------------

# password guess example


# def check_paaword(password):
#     correct_paasword = "gamal123"

#     if password != correct_paasword:
#         print(" your password are false")

#     else:
#         print(" your password are true")


# input_password = input(" enter your password please : ")

# check_paaword(input_password)

# ----------------------------------------------------------------------------

# -----------------------------------------------------
# -----function packing , unpacking argument *Argum----
# -----------------------------------------------------

# x = [1, 2, 3, 4]
# print(x)

# print(*x)

# Ex :1
# def say_hello(n1, n2, n3, n4):
#     peoples = [n1, n2, n3, n4]

#     for name in peoples:
#         print(f" hello {name}")


# say_hello("gamal", "saad", "emad", "ahmed")


# print("=" * 50)


# def say_hello(*peoples): # when don't know number of parameters use *Argument
#     for name in peoples:
#         print(f" hello {name}")


# say_hello("gamal", "saad", "emad", "ahmed", "saber")


# Ex:2


# def my_skill(name, *skills):
#     print(f" I am {name}, I have skills :")

#     for skll in skills:
#         print(f" {skll} ")


# my_skill("gamal", "sql", "Excel", "python")

# print("=" * 50)

# my_skill("saad", "sql", "Excel", "python", "R", "tableau")

# ----------------------------------------------------------------------------------

# -----------------------------------------------------------------
# -----function packing , unpacking argument **kwArgum(keyword)----
# -----------------------------------------------------------------


def my_skill(**skills):  # **skills => should pass Arg as dict
    print(type(skills))
    for skll in skills:
        print(f" {skll} ")


# my_skill(sql="60%", excel="40%", python="90%")

dictskills = {"sql": "60%", "excel": "40%", "python": "90%"}

# my_skill(dictskills) # through error must unpacking Arg (**dictskills)

my_skill(**dictskills)

# ----------------------------------------------------------------------

# -----------------------------------------------------
# -----function default parameters----------------------
# -----------------------------------------------------


# def info(name="unknown", age="unknown", country="unknown"):
#     print(f"my name is {name} has {age} year and from {country} ")


# info("gamal", 26, "ksa")
# info("saad", 24)           # if you don't pass parameter,type default
# info("emad")
# info()
# info("saber", 29, "Egy")

# -------------------------------------------------------------------------
