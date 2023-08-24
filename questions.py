#for even number
'''
a=int(input('enter a number'))
if a%2==0:
   print('number is even')
else:
   print('number is odd')
'''

# to find the simple interest 
'''
p=int(input('enter a number'))
r=int(input('enter a number'))
t=int(input('enter a number'))
s=(p*r*t)/100
print(s)
'''

#to find that person can vote above 18 or not vote less than 18 
'''
name=(input('enter name'))
age=int(input('enter the age'))
if age<18:
    print('person cannot vote')
else:
    print('person can vote')
'''
'''
maths=float(input('enter a number'))
eng=float(input('enter a number'))
science=float(input('enter a number'))
hindi=float(input('enter a number'))
sst=float(input('enter a number'))
total=(maths+eng+science+hindi+sst)/5
if total>85:
    print('Grade A')
elif total<85 and total>=75:
    print('Grade B')
elif total<75 and total>=50:
    print('Grade C')
elif total<30 and total>=50:
    print('Grade D')
elif total<30:
    print('Reappear')
else:
    print('do not print')
'''

'''weight_in_kg=float(input('enter weight in kg'))
height_in_meter=float(input('enter the height in meter'))
BMI=weight_in_kg/(height_in_meter**2)
if BMI>=30:
    print('obese')
elif BMI<30 and BMI>25:
    print('overweight')
elif BMI<25 and BMI>19:
    print('Normal')
elif BMI<19:
    print('Underweight')
else:
    print('nothing')'''

'''
n=int(input('how many times we print'))
for i in range(n):
    r=int(input('enter a number'))
    c=3.14*(r**2)
    print(c)
'''
'''
n=int(input('take the number to print the table'))
for i in range(1,11,1):
    a=(n*i)
    print(n,"*",i,"=",a)
'''
'''
for i in range(10,0,-1):
    print(i)
'''

# to find the factorial of number 
'''
n=int(input('enter a number'))
a=1
for i in range(n,0,-1):
    a=i*a
print(a)
'''

# is to print the number from the range of any number we have to use the logic 
'''
a=int(input('enter a number'))
b=int(input('enter a number'))
for i in range(a,b+1):
    print(i)
'''
'''
a=int(input('enter a number'))
b=int(input('enter a number'))
sum=0
for i in range(a,b+1):
    sum=sum+i
    print(i)
print("total",sum)
'''
'''
e=0
d=0
for i in range(10):
    n=int(input('enter any 10 number'))
    if (n%2==0):
        e=e+1
        print('number is even')
    else:
        d=d+1
        print('number is odd')
print('total even',e)
print('total odd',d)
'''
'''
n=int(input('enter any number'))
f=0
for i in range(2,n):
    if n%i==0:
        f=1
if f==1:
    print('number is not prime')
else:
    print('number is prime')
'''
'''
a=2
b=5
a,b=b,a
print(a,b)
'''
#print the pattern ####
'''
for i in range(4):
    for j in range(4):
        print('#', end='')

    print()
'''
'''
for i in range(4):
    for j in range(i+1):
        print('#', end="")

    print()
'''
'''
for i in range(4):
    for j in range(4-i):
        print('#', end="")

    print()
'''
'''
from array import *

vals = array('i',[5,9,8,7])

newArr = array(vals.typecode, (a for a in vals))

for i in newArr:
    print(i)
'''







    














