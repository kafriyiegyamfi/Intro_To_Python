#!/usr/bin/python
i = 0
while(i < 10):
    i = i + 1
    print (i)
    
a=6
while(a<19):
    a+=1
    print(a)

even=10
while(even%2==0 and even<20):
    even+=2
    print(even)
    
def evens(a,b):
    x=a+1
    while(x>a and x<b):
        if x%2==0:
            print(x)
            x+=1
        else:
            x+=1
        
def reverse_evens(a,b):
    x=b-1
    while(x>a and x<b):
        if x%2==0:
            print(x)
            x-=1
        else:
            x-=1
