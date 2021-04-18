def factorial(number):
    f=1
    for i in range(1, number+1):
        f = f * i
    return f


n=int(input('Enter N : '))
a=[]
for x in range(0,n):
    number=int(input('Enter Number : '))
    a.insert(x,number)

for x in range(0,n):
        print(factorial(a[x]))   
    