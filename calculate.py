#!/usr/bin/python
def calculate(a,b,c):
    answer=0
    a
    if a=='add'or a=='ADD':
      answer=b+c
    
    elif a=='subtract'or a=='SUBTRACT':
        answer=b-c
    elif a=="multiply" or a=='MULTIPLY':
        answer=b*c
    elif a=='divide' or a=='DIVIDE':
        answer=b/c
    else: answer="invalid syntax"
    print( answer)

calculate('add',5,6)
calculate('SUBTRACT',2,9)
calculate('MULTIPLY',2,9)
calculate('DIVIDE',2,9)
    