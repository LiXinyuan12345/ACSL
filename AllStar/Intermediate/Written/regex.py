import re

data1=[
      'asher','aurora','c++','jo-ann',
      'trish','noah2','alb2c3','violet',
      'william','eleanor','yanni','lee',
      ]
pattern1=r'[^bru][a-iro][\D]*[a-n]*[^mr][\d]*'

data2=[
      'bread','cheese','fish','meat',
      'chips','chocolate','cream','pickles',
      'grapes','cookies','coffee','crackers',
      ]
pattern2=r'[^abiou][hro][a-j]*(e|s)*'


data3=[
      'history','classics','physics','botany',
      'geometry','chemistry','mathematics','biology',
      ]
pattern3=r'[a-l]*[e-u]*(cs|y)'

data4=[
      'brush|ing','help/ful','fractals','java',
      'python!','shapeless','igloo','apple',
      "striving","image"
      ]
pattern4=r'[^aeiou]*[aeiou][fghj-np-t]+.(ing|ful|age|less)?'


data= data4
pattern = pattern4
A = 65
a = 97

regex = re.compile(pattern)   
index = 0
index_vec = [] 
for str in data:
    matched =  regex.fullmatch(str)
    if  matched :
        index_vec.append( chr(index+a))
        print(str,end='   ')
    index+=1

print("\n",index_vec)