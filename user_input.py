
# ______________________________
# __________User input__________
# ______________________________


# fname=input("what is your first name ?")
# mname=input("what is your middle name ?")
# lname=input("what is your last name ?")

# fname=fname.strip().capitalize()
# mname=mname.strip().capitalize()
# lname=lname.strip().capitalize()


# print(f"Hello {fname}  {mname:.1s}  {lname} in python course")


#-------------------------
#--------Email------------
#-------------------------

name=input("please enter your name :").strip().capitalize()
Email=input("your please enter your email:").strip()

username=Email[:Email.index("@")]
domain=Email[Email.index("@") + 1:]


print(f"your name is {name}  \nyour email is {Email}")
print(f"your username is {username}  \nyour domain is {domain}")


#-------------------------
#---Age full details------
#-------------------------               

# age=input('what\'s your age :') # input return string (note)
# age=int(input('what\'s your age :'))

# months= age*12
# weeks=months*4
# days=age*365
# hours=days*24
# min=hours*60
# sec=min*60

# print(f"your age details: \nby months {months} \nby weeks {weeks:,} \nby days {days:,} \nby hours {hours:,} \nby minutes {min:,} \nby seconds {sec:,} ")

