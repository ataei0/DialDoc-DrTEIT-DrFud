
#for each i between 0 to 16, the ith index of array a will be 2^i
a = [2**i for i in range(17)]
print('a is:', a)

 #for each x between 1 to 4, the xth index of array b will be x*x (x^2)
b = [x*x for x in range(1,5)]
print('b is:', b)

#for each member of array b if it is even we name it index A, then c[i] is a[A] (c will fill from index 0 till the condition will end)
c = [a[x] for x in b if x%2==0]
print('c is:', c)