import math
print("Введите целое число n")
n=int(input())
print("Введите x")
x=int(input())
S=1
for i in range(1,n+1):
        S=S+((x**i)/(math.factorial(i)))
print("Сумма=",S)
