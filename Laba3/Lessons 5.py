from math import *
 
n = int(raw_input('Enter N:'))
lst = []
i=0
for i in range(1,n):
    count = 0;
    for j in range(1,n):
        if((i%j) == 0):
            count = count + 1;
    if(count == 2) or (count == 1):
        lst.append(i)
for i in lst:
    lst[i] = (2**i)-1
    i = i + 1
for i in lst:
    for i in range(1,n):
        count=0;
        for z in range (1,n):
            if(((lst[i])%z) == 0):
                count = count + 1;
            if (count == 2) or (count == 1):
                print lst
raw_input()
