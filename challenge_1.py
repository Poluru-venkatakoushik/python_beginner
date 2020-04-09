#Take an input string parameter and determine if exactly 3 question marks exist between every pair of numbers that add up to 10. If so, return true, otherwise return false
input_string=input("Enter a string")
def stringcheckker(input_string):
    count_checker=0
    for i in range(1,len(input_string)-2):
        if((input_string[i]==input_string[i+1]==input_string[i+2]=='?') and (int(input_string[i-1])+int(input_string[i+3])==10)):
            count_checker=1
        else:
            continue
    return(bool(count_checker))
print(stringcheckker(input_string))
