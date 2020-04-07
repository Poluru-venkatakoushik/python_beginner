#Q.Find number of pairs (x,y) in an array such that x^y>y^x.
import array as arr
count=0
first_array=arr.array("i",[])
second_array=arr.array("i",[])
first_array_size=int(input("Enter the size of 1st array : "))
second_array_size=int(input("Enter the size of 2nd array : "))
print("Enter the elements of first array")
for i in range(first_array_size):
    ammend_by=int(input("Enter the {0} element of 1st array : ".format(i)))
    first_array.append(ammend_by)
print("\nEnter the elements of Second array")
for i in range(second_array_size):
    ammend_by=int(input("Enter the {0} element of 2nd array : ".format(i)))
    second_array.append(ammend_by)
print("\nFirst array : ")
for i in range(first_array_size):
    print(first_array[i],end=" ")
print("\n\nSecond array : ")
for i in range(second_array_size):
    print(second_array[i],end=" ")
print("\n")
for i in range(first_array_size):
    for j in range(second_array_size):
        if (pow(first_array[i],second_array[j])>(pow(second_array[j],first_array[i]))):
            print("A possible output is [{0},{1}]".format(first_array[i],second_array[j]))