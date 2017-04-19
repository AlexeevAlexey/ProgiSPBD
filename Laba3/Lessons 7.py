import math
y=0
x=0.1
while x <= 2.1:
    print("при х=",round(x,2))
    y=y+(x**2+math.sin(5*x))
    print("y=",round(y,3))
    x=x+0.2
    
    
