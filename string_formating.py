# ______________________________
# ___string formating old way __
# ______________________________

Name="gamal"
l="python"
Ex=10

# print("My name is " + Name + " I am " + l + " developer " ) #concatenate

# print("My name is %s I am %s developer with %d Years Experience" % (Name,l,Ex)) #place holder

# %s => string
# %d => integer
# %f => float

# control floating point number
age=10
# print("My age is %f" % age)
# print("My age is %.2f" % age)

# control string

Name="gamal hisham saad"
# print("My age is %s" % Name)
# print("My age is %.5s" % Name)


# ______________________________
# ___string formating new way __
# ______________________________

Name="gamal"
l="python"
Ex=10


# print("My name is {:s} I am {:s} developer with {:d} Years Experience".format (Name,l,Ex)) #place holder

# {:s} => string
# {:d} => integer
# {:f} => float

# control floating point number
age=10
# print("My age is {:f}".format (age))
# print("My age is {:.2f}".format (age))

# control string

Name="gamal hisham saad"
# print("My age is {:s}".format(Name))
# print("My age is {:.5s}".format(Name))

# format money
money = 5556789345984
# print("My money in bank {}".format(money))
# print("My money in bank {:_}".format(money))
# print("My money in bank {:_d}".format(money))

# Rearrange indexing
a, b, c = "one", "two", "three"
# print("Arrange is : {} {} {}".format(a, b, c))
# print("Arrange is : {1} {2} {0}".format(a, b, c)) #rearrange

x, y, z = 10, 20, 30
# print("Arrange is : {} {} {}".format(x, y, z))
# print("Arrange is : {1} {2} {0}".format(x, y, z))
# print("Arrange is : {1:f} {2:f} {0:f}".format(x, y, z))
# print("Arrange is : {1:.2f} {2:.4f} {0:.6f}".format(x, y, z))

# format in version 3.6+

name = "gamal"
age = 26
# print("My name is {name} and My age is {age}")
# print(f"My name is {name} and My age is {age}")
