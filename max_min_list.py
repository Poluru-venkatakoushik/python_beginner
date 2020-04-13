a=[]
sum=0
n=int(input("enter no.of elements of array:"))
for i in range(n+1):
    temp=int(input("Enter a[{0}]:".format(i)))
    a.append(temp)
    sum+=temp
print("\n")
print("Max:{0}".format(max(a)))
print("Min:{0}".format(min(a)))
print("Difference:{0}".format(max(a)-min(a)))
print("Sum:{0}".format(sum))
print("Average:{0}".format(sum/n))
