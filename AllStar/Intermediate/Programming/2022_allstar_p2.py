import re
import copy
'''

'''

# def  set_color( result1, score1):
#     if  score1-[0] ==1:
#         result1[0].append('b')
#     if  score1-[1] ==1:
#         result1[1].append('b')
#     if  score1-[2] ==1:
#         result1[2].append('b')
def all_elements_in_array(array1, array2):
    set2 = set(array2)  
    for element in array1:
        if element not in set2:
            return False
    return True

scores= [
      [ [0,0,0,0,0]  ],  #score 0
      [ [1,0,0,0,0] ,[0,1,0,0,0] ],  #score 1
      [ [1,1,0,0,0] ,[0,0,1,0,0] ],  #score 2
      [ [1,0,1,0,0] ,[0,1,1,0,0] ,[0,0,0,1,0] ],  #score 3     
      [ [1,1,1,0,0] ,[1,0,0,1,0] ,[0,1,0,1,0] ],  #score 4   
      [ [1,1,0,1,0] ,[0,0,1,1,0] ,[0,0,0,0,1] ],  #score 5
      [ [1,0,1,1,0] ,[0,1,1,1,0] ,[1,0,0,0,1] ,[0,1,0,0,1] ],  #score 6
      [ [1,1,1,1,0] ,[0,0,1,0,1] ],  #score 7           
      [ [1,0,1,0,1] ,[0,1,1,0,1] ,[0,0,0,1,1] ],  #score 8      
      [ [1,1,1,0,1] ,[1,0,0,1,1] ,[0,1,0,1,1] ],  #score 9        
      [ [1,1,0,1,1] ,[0,0,1,1,1]  ],  #score 10     
      [ [1,0,1,1,1] ,[0,1,1,1,1]  ],  #score 11           
]

# hh = 11
# mm = (5 // 5 )
# ss = (10 // 5)
line = input()
params = line.split(":")
hh = int(params[0])
mm = int(params[1]) // 5
ss = int(params[2]) // 5
layout=[]


for candi_h in scores[hh]:   

    result = [ [],[],[],[],[] ]
    for h in range(5):
        if candi_h[h] ==1:
            result[h].append('r')

    for candi_m in scores[mm]:
        copy_m = copy.deepcopy(result)   
        for m in range(5):
            if candi_m[m] ==1:
                result[m].append('g')

        for candi_s in scores[ss]:
            copy_s = copy.deepcopy(result)        
            for s in range(5):
                if candi_s[s] ==1:
                    result[s].append('b')


            item = ""
            for v in result:
                if len(v) == 0 :
                    item += 'k'                
                if len(v) == 1 :
                    item += v[0]
                if len(v) ==3:
                    item += 'w'
                if len(v) == 2:
                    if all_elements_in_array(['r','g'],v):
                        item += "y"
                    if all_elements_in_array(['r','b'],v):
                        item += "m"
                    if all_elements_in_array(['b','g'],v):
                        item += "c"
            layout.append( item )

            result = copy_s
        result= copy_m

layout.sort()
for l in layout:
    print(l,end=" ")            