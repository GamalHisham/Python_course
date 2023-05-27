# print(bool(1))
# print(bool(0))
# print(int(True))
# print(float(True))


# def print_hello():
#     name = "gamal hisham saad"
#     Age = 26
#     Exp = 5
#     print(f"My name is {name}  and I have {Exp} years of Experience")

# print_hello()

# pi = 3.14676533899
# print(pi.__round__(2))


# my_list = [12, "gamal", 10.5, 234]
# # print(len(my_list))
# my_list.append(100)
# print(my_list, len(my_list))
# my_list.extend([200, 300])
# print(my_list, len(my_list))

# my_list.remove(12)
# print(my_list)

# number_list = [2, 3, 4, 7, 1]
# print(max(number_list))
# print(min(number_list))
# print(sum(number_list))
# print(sum(number_list[:2]))

# help(print)

# x = [2, 3, 67, 123, 56]
# print(x.index(67))

# y = x
# y[0] = 1
# print(x)

# y = x[:]
# y[0] = 1
# print(x, y, sep="\n")

my_tuple = (2, 3, 1, 23, 43)
# my_tuple[0] = 12 # through Erorr

#----------------------------------------------------------------------------


inputskills = input (" please enter your skills with rank of them separte between them with comma for Ex: (python,50%,Excel,70%)  ")

inskills = inputskills.split(",")


dictskills = dict(zip(inskills[::2], inskills[1::2])) 


def check_job (dictskills): 

    right_skills = {
        "python":"70%",
        "Excel":"80%",
        "Power_pi":"60%",
    }


    if dictskills == right_skills :

        print(" you are qualified for this job")

    else:

        print(" you are not  qualified for this job")

    
# check_job(dictskills)




