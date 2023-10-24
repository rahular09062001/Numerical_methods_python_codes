#!/usr/bin/env python3

n=int(input("Enter the total number of terms in the function  \n"))

list_1=[]
list_2=[]

for i in range (n):
    print("Enter the coefficent of term number ",i+1)
    k1=float(input())
    print("Enter the power of term number ",i+1)
    k2=float(input())
    list_1.append(k1)
    list_2.append(k2)

print("list_1",list_1)
print("list_2",list_2)

x0=float(input("Enter the lower value of limit \n"))
x1=float(input("Enter the higher value of limit \n"))


def fun(x):
    sum_1=0
    for i in range (n):
        product = list_1[i]*(x**list_2[i])
        sum_1 += product

    return sum_1
x3=0
if(fun(x0)*fun(x1)<0):
    j=0
    while(True):
      j=j+1
      x2 = ((x0*fun(x1))-(x1*fun(x0)))/(fun(x1)-fun(x0))
      if((fun(x2)*fun(x1))<0):
          x0=x2
      else:
            x1=x2
      
      if(abs(x2-x3)<0.0001):
          break
      x3=x2
else:
    print("The upper and lower values of limit are not acceptable")

print("The root = ",x2)
