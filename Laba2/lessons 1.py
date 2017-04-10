A=1
B=0
C=0
a=(A or (not A) and B)or C
b=((not A) or A and (B or C))
c=(A or B and (not C)) and C
print (a)
print (b)
print (c)
