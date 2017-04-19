a =[int(i) for i in input("введите числа через пробел ").split()]
n=int(input("В какую степень вы хотите возвести числа? "))
for i in range(len(a)):
    a[i]=a[i]**n
print("Ваши числа-",a)

    
