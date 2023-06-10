# ----------------------------------
# -------Built In functions part2---
# ----------------------------------

# ---------------------------------------------------
# Map()
# [1] take fun and iterable
# [2] map called map because map the fun in every element
# [3] fun can be pre-defined or lambda fun


# use map with pre-defined fun


def formattext(text):
    return f"- {text.strip().capitalize()} -"


# textlist = ["gamal", "saad", "emad"]

# formated_text = map(formattext, textlist)

# print(formated_text)

# for name in formated_text:
#     print(name)

# for name in map(formattext, textlist):

#     print(name)


# use map with lambda fun


# lam = lambda text: f"- {text.strip().capitalize()} -"
# textlist = ["gamal", "saad", "emad"]

# formated_text = map(
#     lam, textlist
# )  # formated_text = lambda text: f"- {text.strip().capitalize()} -", textlist)


# for name in formated_text:
#     print(name)


# ---------------------------------------------------
# filter()
# [1] take fun and iterable
# [2] filter run the fun in every element
# [3] fun can be pre-defined or lambda fun
# [4] filter out all element which fun return true
# [5] fun need to return boolean value


# def checkname(name):
#     return name.startswith("A")


# mynames = ["Ahmed", "saad", "Attia", "gamal", "Alex"]

# myresult = filter(checkname, mynames)

# for name in myresult:
#     print(name)

# lambda fun

mynames = ["Ahmed", "saad", "Attia", "gamal", "Alex"]

# myresult = filter(lambda name: name.startswith("A"), mynames)

# for name in myresult:
#     print(name)

# --------------------------------------------------------------------
# Reduce() => must import "from functools import reduce"
# [1] take fun and iterable
# [2] run fun with first element and second element and give result
# [3] then run fun with first result and third element
# [4] then run fun with second result and fourth element and so on
# [5] fun can be pre-defined or lambda fun


from functools import reduce

# def sumall(num1, num2):
#     return num1 + num2


# numbers = [1, 2, 5, 7, 100]

# results = reduce(sumall, numbers)  # ((((1+2)+5)+7)+100)

# results = reduce(lambda num1, num2: num1 + num2, numbers)

# print(results)

# ------------------------------------------------------------
# enumerate() # add counter to every element in iterable

# myskills = ["Sql", "Python", "Excel"]

# counterskills = enumerate(myskills)

# for skill in counterskills:
#     print(skill)


# for counter, skill in counterskills:
#     print(f" {counter} - {skill} ")

# ---------------------------------------------------------------------

# help(name of fun)

# print(help(enumerate))

# ---------------------------------------------------------------------
# reversed() => reverse iterable

myskills = ["Sql", "Python", "Excel"]

# for skill in reversed(myskills):
#     print(skill)
