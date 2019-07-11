#!/usr/bin/python

for i in range(1,11):
    print (i)

for j in [1, 2, 3]:
    print (j)

for i in range(1,4):
    print(i)
    
#type(range())=tuple


for i in range (1,5):
    print("****")

for j in [1,2,3,4,3,2,1]:
    print(j*'*')

def contain_a(text):
    for i in text:
        print(i)
        if i=='a':
            return True
    return False

def containSorM(text):
    for i in text:
        print(i)
        if i=='s' and i=='m':
            return True
    return False
    
        

        