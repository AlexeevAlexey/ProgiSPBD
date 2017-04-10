import math
x=float(input("введите координату х "))
y=float(input("введите координату y "))
if (x>=0 and y>=0) or (x<=0 and y>=0):
    if ((-math.fabs(x)+1)<=y) and ((y>=-1) and (y<=1) and (x>=-1) and (x<=1)):
        print ("входит")
    else:
        print ("не входит")
else:
    if ((math.fabs(x)-1)>=y) and ((y>=-1) and (y<=1) and (x>=-1) and (x<=1)):
        print ("входит")
    else:
        print ("не входит")
 
   

