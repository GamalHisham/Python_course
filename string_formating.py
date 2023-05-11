
#______________________________
#___string formating old way __
#______________________________

# Name="gamal"
# l="python"
# Ex=10

# print("My name is " + Name + " I am " + l + " developer " ) #concatenate 

# print("My name is %s I am %s developer with %d Years Experience" % (Name,l,Ex)) #place holder

# %s => string
# %d => integer
# %f => float

# control floating point number
# age=10
# print("My age is %f" % age)
# print("My age is %.2f" % age)

# control string

# Name="gamal hisham saad"
# print("My age is %s" % Name)
# print("My age is %.5s" % Name)



#______________________________
#___string formating new way __
#______________________________

# Name="gamal"
# l="python"
# Ex=10


# print("My name is {:s} I am {:s} developer with {:d} Years Experience".format (Name,l,Ex)) #place holder

# {:s} => string
# {:d} => integer
# {:f} => float

# control floating point number
# age=10
# print("My age is {:f}".format (age))
# print("My age is {:.2f}".format (age))

# control string

Name="gamal hisham saad"
print("My age is {:s}".format(Name))
print("My age is {:.5s}".format(Name))
