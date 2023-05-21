
#------------------------
#----While loop ---------
#while(condition is true):
#     code run
#------------------------

# a=0

# while a < 10:
#     print(a) # while will run when condition is true
#     a += 1

# else:
#     print("while finished") # Else will run when while condition is false



friends=["gamal","saad","alaa","mohamed","eltyeb","hisham","saber","mostafa","hisham","saber"]

x=0

while x < len(friends):

    print(f"# {str(x+1).zfill(2)} {friends[x]}")

    x += 1

else:
    print("all friends printed")

