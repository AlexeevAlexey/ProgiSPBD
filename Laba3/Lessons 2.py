import math
k=int(input ("Введите число k-"))
s=0
v=0
for i in range(-2,k+1):
    g=(((-1)**i)*(math.factorial(i+3)))
    x=(2*(i-4))
    if x==0:
        i=i+1
    else:
        s=s+(g/x)
        v=v+1
        print("Шаг№|",v,"| сумма=",round(s,3))

