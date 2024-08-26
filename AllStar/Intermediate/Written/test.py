import re

def  true_val():

    for a in range(2):
       for b in range(2): 
         for c in range(2):
            aorb=(b or c)
            naorb= (1 if not(b or c) else 0)
            xor1 = aorb ^naorb
            print(a,b,c,aorb ,naorb,xor1 )
   


def f(x):
   if x>=13:
      return f(x-3)+1
   elif x>10:
      return 2*f(x+1)-2
   else:
      return 2*x-4
   
def f(x,y):
    if x>=15:
      return f( int(x/3),int(y/2))+1
    elif x> 8:
      return f(y+4,x-2)
    return x+y


def list1(str1):

    result = []
    for ch in str1:
       if ch in '{[(':
          result.append(ch)
       elif ch in '}])':
          result.pop()

    print(len(result),result)      
          

def ttt():
   s1 = 1
   for x in range(2,11):
      s1 =s1+(x*x)
      y=1
      s2 =1
      while s2 < s1:
         y +=1
         s2+=y
      if s1==s2 :
         print(y)

print( ttt() )

