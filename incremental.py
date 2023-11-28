#incremental development to calculate dispance of two end points

# increment 1
from math import *
x1=int(input('enter'))
y1=int(input('enter'))
x2=int(input('enter'))
y2=int(input('enter'))

#increment 2
def distance():
   d=sqrt(pow((x2-x1),2 )+pow((y2-y1),2)) 
   print('distance=',d)


#increment 3
def distance(x1,y1,x2,y2):
   d=sqrt(pow((x2-x1),2) + pow((y2-y1),2))
   return d
a=distance(x1,y1,x2,y2)
print(a)



