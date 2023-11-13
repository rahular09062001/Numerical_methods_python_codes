#!/usr/bin/env python3

print('''
+---------------------------------------------+
|           LAGRANGE INTERPOLATION            |
+---------------------------------------------+

+---------------------------------------------+
| In this program the function is taken as    |
|   y = f(x)                                  |
+---------------------------------------------+

        ''')

n=int(input("Enter the number of points available : "))

xval=[]
yval=[]

for i in range (0,n,1):
    print("Enter the x value ",i+1)
    x=float(input())
    xval.append(x)
    print("Enter the corresponding y value")
    y=float(input())
    yval.append(y)

print("x : ",xval)
print("y : ",yval)

x1=float(input("Enter the value of x for which y has to be calculated.  : "))

s=0
for i in range (0,n,1):
    p=1
    for j in range (0,n,1):
        if(i is not j):
            p=p*((x1 - xval[j])/(xval[i]-xval[j]))

    s = s + (p*yval[i])

print("Result = ",s)


