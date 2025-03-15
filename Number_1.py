my_list=[1,3,2,6,8,9,11,13,4,5,7,6,3,4,15,21,34]
a=[]
b=[]
c=[]
for i in range (len(my_list)):
    if my_list[i]<5:
        a.append(my_list[i])
    b.append(my_list[i]/2)
    if my_list[i]>17:
        c.append(my_list[i]*2)
print("1)",a)
print("2)",b)
print("3)",c)
number=int(input("Введите число: "))
print("4)", [i**2 for i in range(number+1)])
print("5)", " ".join(str(int(i)**2) for i in input("Введите числа через пробел: ").split()))
print("6)", " ".join(str(int(i)**2) for i in input("Введите числа через пробел: ").split() if (int(i)**2)%10!=9 and int(i)%2!=0))




