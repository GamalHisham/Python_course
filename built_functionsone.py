# ----------------------------------
# -------Built In functions part1---
# ----------------------------------

# all() => check if all element in iterable is true

# x = [1, 2, 3, 4, 0]

# if all(x):
#     print("all elements is true")

# else:
#     print("there's one elemnt is false ")

# ----------------------------------------------
# any() => check if one element in iterable is true

# x = [0, [], 0]

# if any(x):
#     print("all elements is true")

# else:
#     print("there's one elemnt is true ")
# ----------------------------------------------

# bin() => tell me binary code of integer number

# print(bin(12))
# ----------------------------------------------

# id() => all object in memory has id

# x = 1
# y = 23

# print(id(x))
# print(id(y))

# ----------------------------------------------

# sum() => sum elements in iterable

# x = [12, 33, 44, 55]

# print(sum(x))
# print(sum(x,10)) # sum elements and add 10

# ----------------------------------------------

# round() => round float numbers

# print(round(123.345))
# print(round(123.345, 2))
# print(round(123.346, 2))

# ----------------------------------------------

# range(start,end,step)

# print(list(range(10)))
# print(list(range(1, 10)))
# print(list(range(0, 10, 2)))

# ----------------------------------------------

# print() => very imp

# print("gamal hisham saad")

# print("gamal", "hisham", "saad", sep="|") => default space " "

# print("first line", end="\n")   # => default \n
# print("first line", end=" ")
# print("second line")
# print("third line")

# ----------------------------------------------

# abs()
# print(abs(112))
# print(abs(-124))

# ----------------------------------------------

# pow()
# print(pow(2,4))

# ----------------------------------------------

# min()
# x = (1, 23, -1, 45)
# print(min(12, 33, -12, 344))
# print(min("a", "z", "f", "gamal"))
# print(min("z", "h", "gamal"))
# print(min(x))

# ----------------------------------------------

# max()
# x = (1, 23, -1, 45)
# print(max(12, 33, -12, 344))
# print(max("a", "z", "f", "gamal"))
# print(max("z", "h", "gamal"))
# print(max(x))

# ----------------------------------------------

# slice()

# x = ["a", "b", "c", "d", "e", "f"]

# print(x[:5])
# print(x[slice(5)])
# print(x[slice(1, 5)])

# ----------------------------------------------
