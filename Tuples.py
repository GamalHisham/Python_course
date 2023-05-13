
# ______________________________
# ___________Tuples_____________
# 1- Tuple enclosed in parnetheses () , can remove parnetheses if you want
# 2- Tuple are ordered ,use index to access items
# 3- Tuple are Immutable => you can't add,delete,Edit
# 4- Tuple items is not unique ("one","two","one")
# 5- Tuple can have different data types
# 6- operators used in string and list used also in tuple
# ______________________________

# my_tuple=("gamal",12,10.5,True)
# My_tuple="gamal",12,10.5,True #can remove parnetheses if you want
# print(my_tuple)
# print(My_tuple)
# print(type(my_tuple))
# print(type(My_tuple))
# print(my_tuple[0])
# my_tuple[1]=20 #'tuple' object does not support item assignment (Immutable)

# Tuple with one element
# x=("gamal")
# y="gamal"
# print(type(x)) #<class 'str'>
# print(type(y)) #<class 'str'>

# x=("gamal",)
# y="gamal",
# print(type(x)) #<class 'tuple'
# print(type(y)) #<class 'tuple'

# Tuple concatenation
# x=(1,2,45)
# y=(3,56,4)

# c= x + y
# print(c)

# Tuple,list,string Repeat (*)
# mystring="gamal"
# mylist=["gamal"]
# mytuple=("gamal")
# print(mystring*3)
# print(mylist*3)
# print(mytuple*3)

# ______________________________
# __________Tuple Method________
# ______________________________

# count()
# x=(1,3,4,5,1,2,1,567,1)
# print(x.count(1))


# # index()
# x=(1,3,4,5,1,2,1,567,1)
# print("the position of index is : {:d} " .format(x.index(4)))

# Tuple Destruct
# a=(1,2,3)
# x,y,z,=a 
# print(x,y,z,sep="\n")
# print(x,y,z,sep="\n") #many values to unpack (expected 3)
# a=(1,2,3,12)
# x,y,z=a 
# print(x,y,z,sep="\n") #many values to unpack (expected 3)
# x,y,z,_=a 
# print(x,y,z,sep="\n")
