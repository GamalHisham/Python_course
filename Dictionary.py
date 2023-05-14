# ______________________________
# _______Dictionary_____________
# 1- Dict enclosed in curly braces
# 2- Dict ietems contains key : value
# 3- Dict key is Immutable =>(numbers,string,list) list not allowed
# 4- Dict value can have any data type
# 5- Dict key is unique
# 6- Dict not ordered Access element with key
# ______________________________

user = {
    "name": "gamal",
    "Age": 26,
    "Countary": "Egypt",
    "Rating": 10.5,
    "Skills": ["python", "Sql", "Tableau"],
}

# print(user)

# Access element with key
# print(user["name"])
# print(user.get("Countary"))

# get dict keys
# print(user.keys())


# get dict values
# print(user.values())


# two dimensional dict

names = {
    "one": {"name": "gamal", "age": 26},
    "second": {"name": "ahmed", "age": 36},
    "three": {"name": "mostafa", "age": 32},
}

# print(names)
# print(names["one"])
# print(names["second"]["name"])


# dict length
# print(len(names))
# print(len(names["second"]))


# add multi dict
one = {"name": "gamal", "age": 26}

two = {"name": "saad", "age": 24}

three = {"name": "emad", "age": 17}

allnames = {"first": one, "second": two, "third": three}

# print(allnames)


# ______________________________
# __________Dict Method_________
# _______________________________

# clear()
user = {"name": "gamal"}

# print(user)
# user.clear()
# print(user)

# update()
user = {"name": "gamal"}
# print(user)
# user.update({"age": 26})
# print(user)
# user["language"] = "python"
# print(user)

# copy()
main = {"name": "gamal"}

sub = main.copy()  # Shallow copy
# print(sub)

# main.update({"skills": "excel"})
# print(main)
# print(sub)


# setdefault()
user = {"name": "gamal"}
# print(user)
# print(user.setdefault("name", "saad"))
# print(user.setdefault("age", 26))
# print(user)

# popitem() # print last item in dict
user = {"name": "gamal", "age": 26}
# print(user)
# print(user.popitem())


# items()
user = {"name": "gamal", "age": 26}
alluser = user.items()
# print(user)
user.update({"skill": "sql"})
# print(alluser)


# fromkeys()
keys = ("one", "two", "three")
values = (1, 2, 3)
x = dict.fromkeys(keys, values)
# print(x)
