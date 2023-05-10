

#________________________________
#_______ string methods___________
#________________________________



#len()
x="gamal hisham saad"
print(len(x))


#strip(),rstrip(),lstrip()
x=" gamal hisham saad "
y="gamal hisham saad "
z=" gamal hisham saad"
print(x.strip()) #remove spaces from right and left
print(y.rstrip()) #remove spaces from right 
print(z.lstrip()) #remove spaces from  left


#title(),capatilize()
x="gamal hisham saad"
print(x.title())
print(x.capitalize())


#upper(),lower()
x="gamal hisham saad"
y="GAMAL HISHAM SAAD"

print(x.upper())
print(y.lower())


#split(),rsplit()
x="gamal hisham saad"
print(x.split())
x="gamal-hisham-saad-hashem"
print(x.split("-",2))
x="gamal-hisham-saad-hashem"
print(x.rsplit("-",2)) #2 split from right


#center()
x="gamal"
print(x.center(9)) #must added one argument
print(x.center(9,"$"))



#count()
x="i love python because python clera and easy"
print(x.count("python")) # 2 python words
print(x.count("python" ,0,18)) # only one python (give start and end index to research)



#swapcase()
x="i lovE pYthon"
y="I love Python"
print(x.swapcase())
print(y.swapcase())


#startwith()
x="i love python"
print(x.startswith("i"))
print(x.startswith("s"))
print(x.startswith("l",2,7))

#endwith()
x="i love python"
print(x.endswith("n"))
print(x.endswith("s"))
print(x.endswith("e",2,6))

