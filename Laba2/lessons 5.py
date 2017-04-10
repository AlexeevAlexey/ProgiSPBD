a=float(input("введите коэффицент а "))
b=float(input("введите коэффицент b "))
c=float(input("введите свободный член с "))
if a != 0:
    d=(b**2-4*a*c)**(1/2)
    x1=(-b-d)/(2*a)
    x2=(-b+d)/(2*a)
    print("дискриминант =",d)
    if x1 == x2:
        print("корень = ",-x1)
    else:
        print("первый корень = ",x1)
        print("второй корень = ",x2)
else:
    print ("a равно нулю 0")
    





    
