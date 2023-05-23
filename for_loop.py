
# -------------------------------
# ----------for loop ------------
# for item in iterable object:
#     Do somthing with item
# -------------------------------


# numbers = [1,2,3,4,5,6,7,8,9]

# for num in numbers :


#     if num % 2 == 0 :

#         print(f" the number {num} is even ")

#     else :

#         print(f" the number {num} is odd ")

# else :
#     print("loop are finished")  # Run when loop finish oppisite while loop 'else' run when condition is false


#-----------------------------------------------------------------------------------------------

# -------------------------------
# --------Examples---------------
# -------------------------------


# myskill = {
#     "excel": "90%",
#     "python": "100%",
#     "sql": "80%",
#     "power pi": "70%",
# }

# # print(myskill["excel"])
# # print(myskill.get("python"))


# for skill in myskill :

#     print(f" My {skill} skill has a progress : {myskill[skill]} " )

#-----------------------------------------------------------------------------------------------------

# -------------------------------
# ---------Nested loop-----------
# -------------------------------


employee = {
    "gamal":{
        "python": "90%",
        "Excel": "95%",
        "sql": "85%",
    },
    "ahmed":{
        "python": "50%",
        "Excel": "60%",
        "sql": "70%",
    },
    "saad":{
        "python": "100%",
        "Excel": "40%",
        "sql": "75%",
    },

}

# print(employee["saad"])
# print(employee["saad"]["python"])


# for emp in employee :
#     print(f"{emp} has skills :  ")

#     for skill in employee[emp]:
#         print(f" - {skill} => {employee[emp][skill]} ")


# the same solution

# for emp , skill  in employee.items():

#     print(f"{emp} has skills :  ")

#     for sub_emp , sub_skill in skill.items():

#         print(f" - {sub_emp} => {sub_skill} ")




#---------------------------------------------------------------------

# -------------------------------
# ------Break,continue,pass------
# -------------------------------


# number = [1,2,3,4,5,6,7,8,9,10]

# # continue 
# for num in number :
#     if num == 9:
#         continue

#     print(num)

# print("=" * 50)

# # Break 
# for num in number :
#     if num == 9:
#         break

#     print(num)


# print("=" * 50)

# # pass 
# for num in number :
#     if num == 9:
#         pass

#     print(num)

