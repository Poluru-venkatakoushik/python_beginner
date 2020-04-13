from datetime import date
import math
print("Today is ",date.today())
print('''
                                            WELCOME!
                                    Enter two numbers when asked    
                                    Then mention the operation to be done
                                    Enter the operation to be done
            ''')
inp_1=int(input("Enter the first number"))     #user inputs the first number
inp_2=int(input("Enter the second number"))    #user inputs the second number
print('''
                                    Enter d for division
                                          m for multiplication
                                         md for remainder of 1st /2nd 
                                          a for addition
                                          s for subtraction
                                          f for factorial
                                          p for percentage of each in sum
                                          
    
    ''')
operator=input("Enter the operator ")
if(operator.upper()=="D"):
    print("Result :{0:>5}".format(inp_1 / inp_2))
elif(operator.upper()=="M"):
    print("Result :{0:>5}".format(inp_1*inp_2))
elif(operator.upper()=="MD"):
    print("Result :{0:>5}".format(inp_1//inp_2))
elif(operator.upper()=="A"):
    print("Result :{0:>5}".format(inp_1+inp_2))
elif(operator.upper()=="S"):
    print("Result :{0:>5}".format(inp_1-inp_2))
elif(operator.upper()=="F"):
    print("Result :{0:>5}{1:>5}".format(math.factorial(inp_1),math.factorial(inp_2)))
else:
    print("In sum of the inputted numbers the percentage of 1st input ={0:>10} 2nd input={1:>10}".format(inp_1/(inp_1+inp_2),inp_2/(inp_1+inp_2)))