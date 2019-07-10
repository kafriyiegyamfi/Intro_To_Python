#!/usr/bin/python
import math

raduis=float(input("please enter the value of the raduis of the circle: "))

surfaceArea= 4*math.pi*(raduis**2)
print("the surface area is :"+str(surfaceArea))

volume = (4/3)*math.pi*(raduis**3)

print('The volume is :'+str(volume))


