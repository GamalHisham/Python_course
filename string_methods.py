# ________________________________
# _______ string methods__________
# ________________________________


# len()
x = "gamal hisham saad"
# print(len(x))


# strip(),rstrip(),lstrip()
x = " gamal hisham saad "
y = "gamal hisham saad "
z = " gamal hisham saad"
# print(x.strip())  # remove spaces from right and left
# print(y.rstrip())  # remove spaces from right
# print(z.lstrip())  # remove spaces from  left


# title(),capatilize()
x = "gamal hisham saad"
# print(x.title())
# print(x.capitalize())


# upper(),lower()
x = "gamal hisham saad"
y = "GAMAL HISHAM SAAD"

# print(x.upper())
# print(y.lower())

#  swapcase()
x = "i lovE pYthon"
y = "I love Python"
# print(x.swapcase())
# print(y.swapcase())



# split()
x = "gamal hisham saad"
# print(x.split())
# x = "gamal-hisham-saad-hashem"
# print(x.split("-", 2))

# rsplit()
x = "gamal-hisham-saad-hashem"
# print(x.rsplit("-", 2))  # 2 split from right


# center()
x = "gamal"
# print(x.center(9))  # must added one argument
# print(x.center(9, "$"))

# rjust(),ljust()
x = "gamal"
# print(x.rjust(10))
# print(x.rjust(10, "#"))
# print(x.ljust(10, "#"))


# count()

x = "i love python because python clear and easy"
# print(x.count("python"))  # 2 python words
# print(x.count("python", 0, 18))  # only one python (give start and end index to research)
 


#  startwith()
x = "i love python"
# print(x.startswith("i"))
# print(x.startswith("s"))
# print(x.startswith("l", 2, 7))

# # endwith()
x = "i love python"
# print(x.endswith("n"))
# print(x.endswith("s"))
# print(x.endswith("e", 2, 6))

#  index()
x = "i love python"
# print(x.index("p"))
# print(x.index("p", 0, 10))
#  print(x.index("p", 0, 5)) #through error

#  find()
x = "i love python"
# print(x.find("p"))
# print(x.find("p", 0, 10))
# print(x.find("p", 0, 5))  # through -1 and excute code without error

# splitlines()
# x = """gamal
# hisham
# saad"""
# print(x.splitlines())

x = "gamal\nhisham\nsaad"
# print(x.splitlines())

# expandtabs()
x = "i\tlove\tpython"
# print(x)
# print(x.expandtabs(1))


# istitle(),islower(),isspace() (Answering true or false)
x = "I Love Python"
# print(x.istitle())
x = " "
# print(x.isspace())
X = "I Love Python"
# print(x.islower())

x = "gamal_hisham"
# print(x.isidentifier())

x = "gamal--hisham"
# print(x.isidentifier())


x = "python"
# print(x.isalpha())

x = "python123"
# print(x.isalpha())

x = "python"
# print(x.isalnum())

x = "python123"
# print(x.isalnum())


# replace()
x = "one two three one two three"
# print(x.replace("one", "1"))
# print(x.replace("one", "1", 1))

# join() convert iterable to string
x = ["gamal", "hisham", "saad"]
# print("-".join(x))
# print(" ".join(x))
# print(type("-".join(x)))


