import re

def  f(x,y):
   if x >=10:
      return f( int(x/2),y-1)+3
   elif x>5:
      return 2*f(x+1,int(y/3))
   else:
      return x*y

print( f(24,6) )

   
        

