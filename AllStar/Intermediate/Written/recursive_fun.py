import re

def  f(x,y):
   if x <y :
      return f(x+1,y-2)+f(y,x)+1
   elif x==y:
      return f(f(x/2,y),x/2)-3
   else:
      return x-y


print( f(14,20) )

   
        

