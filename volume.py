import array as arr
array_main=arr.array('i',[])
array_size=int(input("Enter the size of array : "))
for i in range(array_size):
    ammend_val=int(input("Enter element of array at index {0} : ".format(i)))
    array_main.append(ammend_val)
for i in range(array_size):
    print(array_main[i],end='')
sum=int(input("Sum : "))
for i in range(array_size):
    for j in range(i,array_size):
        if((array_main[i]+array_main[j])==sum):
            print("A possible pair is :[{0},{1}]".format(i,j))