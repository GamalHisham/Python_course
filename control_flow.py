# ______________________________
# ________Control flow__________
# ________If-Elif-Else__________
# ______________________________


# uname = input("What's your name : ").strip().capitalize()
# cname = input("what's your course name : ").strip()
# ncountry = input("Enter your country please : ").strip()
# pcourse = 100


# if ncountry == "egypt":
#     print(
#         f'Hello {uname} in "{cname}" because you are from {ncountry} price of course is {pcourse-90}'
#     )

# elif ncountry == "ksa":
#     print(
#         f'Hello {uname} in "{cname}" because you are from {ncountry} price of course is {pcourse-80}'
#     )

# elif ncountry == "emirates":
#     print(
#         f'Hello {uname} in "{cname}" because you are from {ncountry} price of course is {pcourse-70}'
#     )

# else:
#     print(
#         f'Hello {uname} in "{cname}" because you are from {ncountry} price of course is {pcourse-50}'
#     )


uname = input("What's your name : ").strip().capitalize()
ncountry = input("Enter your country please : ").strip()
cname = input("what's your course name : ").strip()
isstudent = input("Are you student Y/N : ").strip()
pcourse = 100

if ncountry == "egypt" or ncountry == "ksa" or ncountry == "emirates":
    if isstudent == "Y":
        print(
            f'Hello {uname} in "{cname}" because you are from {ncountry} and are you student price of course is {pcourse-90}'
        )
    else:
        print(
            f'Hello {uname} in "{cname}" because you are from {ncountry} price of course is {pcourse-80}'
        )


else:
    print(
        f'Hello {uname} in "{cname}" because you are from {ncountry} price of course is {pcourse-50}'
    )
