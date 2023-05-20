
# ______________________________
# ____Membership operators______
# ____ in & not in______________
# ______________________________

# string
# name="gamal"
# print("g" in name)
# print("m" in name)
# print("f"  not in name)

# list 
# friends=["saad","ahmed","emad"]
# print("saad" in friends)

# print("saad" not in friends)



#---------------------
#----admin login------
#---------------------

# admin list
admin = ["Gamal","Saad","Ahmed","Ali","Mostafa","Saber","Mahmoud"]

# login 
name = input("please write your name : ").strip().capitalize()

if name in admin :
    print("welcome you are admin ")

    option = input("you want to \"update\" or \"delete\" : ").strip()
    if option == "update":
        newname = input("please write new name : ").strip().capitalize()
        admin[admin.index(name)]=newname
        print(" \"admin updated\" ")
        print(admin)

    elif option == "delete":
        admin.remove(name)
        print("\"admin deleted\" ")
        print(admin)
    

else :
    print(" welcome you are not admin ")

    status = input(" Do you want add or not (Y-N) : " ).strip().capitalize()
    if status == "Y" :
        admin.append(name)
        print(" you are added ")
        print(admin)

    else :
        print(" you are not added ")

