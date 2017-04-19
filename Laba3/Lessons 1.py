a=int(input ("Введите число А-"))
b=int(input ("Введите число B-"))
if b>a:
    arr = []
    for i in range(a,b+1):
        arr.append(i)
    print(arr)
    print("количество целых чисел-",len(arr))
else:
    print("число 'B' должно быть больше 'A'")
