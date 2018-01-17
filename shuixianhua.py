#shuixianhua

num=int(input("please enter a num:"))
i=num%10
k=int(num/100)
j=int((num-k*100-i)/10)

print(i,j,k)

if (num==i**3+j**3+k**3):
    print("The numer is ShuiXianHua!!")
else:
    print("Oh,Sorry,You are wrong!")
