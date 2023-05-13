# ______________________________
# ___________Sets_____________
# 1- Set enclosed in Curly braces {}
# 2- Set are not ordered ,not indexing  to access items and slicing
# 3- Set has immutable data type (numbers,strings,Tuples) list and dict are not
# 4- Set items is  unique
# ______________________________

# myset={1,"gamal",23,"saad"}
# print(myset)
# print(myset[0]) #'set' object is not indexing

# myset={"gamal",23,10.5,[1,34,3]}
# print(myset) #(Set has immutable data type list and dict are not)

# myset={"gamal",23,10.5,(1,34,3)}
# print(myset)

# myset={"gamal",23,10.5,"gamal"}
# print(myset)#Set items is  unique (print one "gamal")


# ______________________________
# __________Set Method________
# ______________________________

# clear()
# x={1,2,3}
# x.clear()
# print(x)

# union()
# a={1,2,3}
# b={"one","two","three"}
# c={"zero"}
# print(a.union(b,c))
# print(a | b | c) # | (shift+back clash)

# add()
# x={1,2,3}
# x.add(4)#add one argument
# print(x)

# copy() shallow copy
# x={1,2,3}
# y=x.copy()
# print(x)
# print(y)

# remove()
# x={1,2,3}
# x.remove(3)
# print(x) #through error if don't find element

# discard()
# x={1,2,3}
# x.discard(7)
# print(x) # don't through error if don't find element

# pop()
# x={1,2,3}
# print(x.pop()) #print random element

# update()
# x={1,2,3}
# y={'gamal',1,12}
# x.update(["saad"]) # can update with list
# x.update(y)
# print(x) #such as union


# difference()
# x = {1, 2, 3}
# y = {1, "gamal", 234}
# print(x)
# print(x.difference(y)) # x-y
# print(x)

# difference_update()
# x = {1, 2, 3}
# y = {1, "gamal", 234}
# print(x)
# x.difference_update(y)
# print(x)

# intersestion()
# x = {1, 2, 3, 4}
# y = {1, 45, 23, 2}
# print(x)
# print(x.intersection(y)) # x & y
# print(x)

# intersestion_update()
# x = {1, 2, 3, 4}
# y = {1, 45, 23, 2}
# print(x)
# x.intersection_update(y)  # x & y
# print(x)

# symmetric_difference()
# x = {1, 2, 3, 4, "gamal"}
# y = {1, 45, 23, 2}
# print(x)
# print(x.symmetric_difference(y))  # x ^ y
# print(x)

# symmetric_difference_update()
# x = {1, 2, 3, 4, "gamal"}
# y = {1, 45, 23, 2}
# print(x)
# x.symmetric_difference_update(y)  # x ^ y
# print(x)


# issuperset()
# x = {1, 2, 3, 4}
# y = {1, 2, 3}
# print(x.issuperset(y))


# issubset()
# x = {1, 2, 3, 4}
# y = {1, 2, 3}
# print(y.issubset(x))


# isdisjoint()
# x = {1, 2, 3, 4}
# y = {1, 2, 3}
# z = {20, 123, 45}
# print(x.isdisjoint(y))
# print(x.isdisjoint(z))
