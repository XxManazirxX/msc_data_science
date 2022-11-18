import math
def hypotenuse(x,y):
   # Returns the hypotenuse of a
   # triangle with sides x,y 
   hyp = math.sqrt(x**2+y**2)
   return hyp

a = 5
b = 12
h = hypotenuse(a,b)
print (h)

