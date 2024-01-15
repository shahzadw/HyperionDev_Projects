#entering the lengths of a triangle 
side_1 = input ("enter the length of side 1: ")
side_2 = input ("enter the length of side 2: ")
side_3 = input ("enter the length of side 3: ")
a = int(side_1)
b= int(side_2)
c= int(side_3)
#since triangle has 3 side, semi perimeter is calculated using the formula 
import math 
s = (a + b + c)/2
print (s)
area_nosqt = s*(s-a)*(s-b)*(s-c)
area = math.sqrt(area_nosqt)
display = "the area of the triangle is: {}".format(area)
print (display)





