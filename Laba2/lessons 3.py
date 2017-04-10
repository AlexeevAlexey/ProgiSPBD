import math
a=int(input("введите 1 число "))
b=int(input("введите 2 число "))
c=math.fmod(a + b,2)
if c == 1:
    print('true')
else:
    print ('false')

    
a=int(input("введите 1 число "))
b=int(input("введите 2 число "))
c=int(input("введите 3 число "))
d=math.fmod(a,3)
f=math.fmod(b,3)
g=math.fmod(c,3)
if d == f == g == 0:
   print ('true')

else:
    print ('false')


