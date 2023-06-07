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

myresult = filter(lambda name: name.startswith("A"), mynames)

for name in myresult:
    print(name)
