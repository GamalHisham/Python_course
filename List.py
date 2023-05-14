# ______________________________
# ___________List_______________
# 1- list enclosed in square brackets []
# 2- list are ordered ,use index to access items
# 3- list are Mutable => add,delete,Edit
# 4- list items is not unique ["one","two","one"]
# 5- list can have different data types
# ______________________________


my_list = ["one", 12, 10, 12.23, True]

# print(my_list)#['one', 12, 10, 12.23, True]
# print(my_list[0])#one
# print(my_list[-1])#True
# print(my_list[0:3])#['one', 12, 10]
# print(my_list[::1])#['one', 12, 10, 12.23, True]
# print(my_list[::2])#['one', 10, True]


# print(my_list)
# # my_list[-1] = False
# my_list[0:3] = ["two"]  # it is not necessary add three items
# print(my_list)


# ______________________________
# __________List Method_________
# _______________________________

# append()
friends = ["gamal", "ahmed", "saad"]
new_friends = ["mahmoud", "mostafa"]
# friends.append("mohamed")
# friends.append(new_friends)
# print(friends)
# print(friends[0])
# print(friends[-1])
# print(friends[-1][1])

# extend()
# friends.extend(new_friends)
# print(friends)

# remove()
# x = [1, 2, 3, 4, 6, 2, 45, 2]
# x.remove(2) # remove first 2 only
# print(x)

# sort() => sorting Numbers and string
# x = [120, 3, 23, -12, 0, 15]
# x.sort()
# print(x)
# x.sort(reverse=False)
# print(x)
# x.sort(reverse=True)
# print(x)

# reverse()
# x = ["gamal", 12, 45, 67, "saad"]
# x.reverse()
# print(x)

# clear()
# x = [1, 3, 2, 6, 9]
# x.clear()
# print(x)

# copy
# x = [1, 2, 3]
# y = x.copy()
# print(x)  # main list
# print(y)  # copied list
# x.append(4)
# print(x)
# print(y)

# count()
# x = [2, 1, 45, 67, 2, 1, 34, 1]
# print(x.count(1))

# index()
# friends = ["gamal", "ahmed", "saad"]
# print(friends.index("saad"))

# insert()
# x = [2, 1, 45, 67]
# x.insert(0, "test")  # add "test" before index 0
# print(x)

# pop()
x = [2, 1, 45, 67]
# print(x.pop(0))
# print(x[0])
# print(x.pop(-1))
# print(x[-1])
