# ------------------------
# ----While loop ---------
# while(condition is true):
#     code run
# ------------------------

# a=0

# while a < 10:
#     print(a) # while will run when condition is true
#     a += 1

# else:
#     print("while finished") # Else will run when while condition is false


#--------------------------------------------------------------------------------------------------------------

friends=["gamal","saad","alaa","mohamed","eltyeb","hisham","saber","mostafa","hisham","saber"]

x=0

while x < len(friends):

    print(f"# {str(x+1).zfill(2)} {friends[x]}")

    x += 1

else:
    print("all friends printed")


#-------------------------------------------------------------------------------------------------

# --------------------------------
# ----Bookmark Manage Example-----
# --------------------------------

# Empty list for websites
websites = []

# maximum added websites
maxwebsites = 3

while maxwebsites > 0:
    # input website
    addwebsites = input('please enter website without "https:" :').strip().lower()
    websites.append(f"https//{addwebsites}")

    maxwebsites -= 1

    print(websites)
else:
    print("list are full")

print("=" * 50)


# print website list element

if len(websites) > 0:
    websites.sort()
    index = 0

    while index < len(websites):
        print(websites[index])
        index += 1


#--------------------------------------------------------------------------------------------


# ------------------------------------
# ----Password Guess Example----------
# ------------------------------------


tries = 3
correctpassword = "gamal"

inputpassword = input(" Enter your password : ")

while inputpassword != correctpassword :
    tries -= 1 
    print(f" wrong password , you have {'last' if tries==0 else tries} chance ")

    inputpassword = input(" Enter your password : ")

    if tries == 0 :

        break

else:
    print("correct password")




