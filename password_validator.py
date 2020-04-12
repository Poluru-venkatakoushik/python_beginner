#password validity checker
#1.checks if the password is atleast 8 characters long and atmost 13 characters long
#2.atleast one upper and lower case and digit
#3.Atleast one of @#$ characters
from time import sleep
password=input('Enter a password :  ')
len_check=0
upper_check=0
lower_check=0
special_check=0
if(len(password) in range(8,14)):
    len_check=1
for i in range(len(password)):
    if(ord(password[i]) in range(65,92)):
        upper_check=1
    elif ((ord(password[i]) in range(97,123))):
        lower_check=1
    elif(password[i]=='@'or'#'or'$'):
         special_check=1
if(len_check==1 and upper_check==1 and lower_check==1 and special_check==1):
    print("Valid password")
else:
    print("Invalid password")
    sleep(3)
    quit()
