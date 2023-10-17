#!/usr/bin/env python3

def fn(x):
    a = x**2 + x -7

    return a

i = 0
x0 = 0
x1 = 0
x2 = 0

x0 = float(input("Enter the lower limit for calculation \n"))

x1 = float(input("Enter the upper limit for calculation \n"))

if(fn(x0)*fn(x1) < 0):
    print("The range is acceptable")

    while True:

        print(i," ",x0," ",x1," ",x2,"",fn(x2))

        i=i+1

        x2 =(x1+x0)/2.0

        if(fn(x0)*fn(x2) < 0):

            x1 = x2

        else:

            x0 = x2



        if(abs(x1-x0)<=0.0001):
            print("-----------------------")
            print("Root = ",x2)
            print("------------------------")
            break



else:
    print("The range is not acceptable")
