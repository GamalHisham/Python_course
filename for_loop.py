
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


myskill = {
    "excel": "90%",
    "python": "100%",
    "sql": "80%",
    "power pi": "70%",
}

# print(myskill["excel"])
# print(myskill.get("python"))


for skill in myskill :

    print(f" My {skill} skill has a progress : {myskill[skill]} " )

