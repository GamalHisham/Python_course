
# ______________________________
# ______Type conversion_________
# ______________________________


# str()

x=10
print(type(x))
print(type(str(x)))

print("=" * 50)

# Tuple()

a = "gamal" #string
b = [1,2,3,4] #list
c = {'a','b','c'} # set
d = {"one":1,"two":2} #dict

print(tuple(a))
print(tuple(b))
print(tuple(c))
print(tuple(d))


print("=" * 50)

# list()

a = "gamal" #string
b = (1,2,3,4) #tuple
c = {'a','b','c'} # set
d = {"one":1,"two":2} #dict

print(list(a))
print(list(b))
print(list(c))
print(list(d))

print("=" * 50)

# set()

a = "gamal" #string
b = (1,2,3,4) #tuple
c = ['a','b','c'] # list
d = {"one":1,"two":2} #dict

print(set(a))
print(set(b))
print(set(c))
print(set(d))


print("=" * 50)

# dict()

# a = "gamal" #string
# d = {{"one",1},{"two",2}} #unhashable type: 'set'  (don't convert to dict)
# print(dict(a)) #don't convert to dict(must have key and value)
# print(dict(d))

# only list & tuple convert to dict 
b = (("a",1),("b",2)) # Nested tuple (have key and value) to convert to dict
c = [["one",1],["two",2]] # Nested list (have key and value) to convert to dict

print(dict(b))
print(dict(c))


