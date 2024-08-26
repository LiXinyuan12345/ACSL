import re
from functools import cmp_to_key

def get_diagonals(matrix,size):

    num_rows = len(matrix)
    num_cols = len(matrix[0])
    result = []

    v=max(num_rows,num_cols)
    for d in range(-v + 1, num_cols):
        diag = [(r, c) for r in range(num_rows) for c in range(num_cols) if r - c == d]
        if len(diag) >= size:
            result.append(diag)

    for d in range(num_rows + num_cols - 1):
        diag = [(r, c) for r in range(num_rows) for c in range(num_cols) if r + c == d]

        if len(diag) >= size:
            result.append(diag)
    return result


def  diagonals_find_word(word,grid):    

    result = get_diagonals(grid,len(word))
    if len(result)<= 0 :
        return 

    word_width = len(word)
    i = 0
    for coords in result:
        for start in range(0,len(coords)-word_width+1):
            equl = True
            for i in range(word_width):
                r = coords[start+i][0]
                c = coords[start+i][1]
                if word[i] != grid[r][c][0]:
                    equl = False
                    break

            if equl == True:
                for i in range(word_width):
                    r = coords[start+i][0]
                    c = coords[start+i][1]
                    grid[r][c][1]  = True       
                #print(word)             
                return True        

    i = 0
    for coords in result:
        for start in range(0,len(coords)-word_width+1):            
            equl = True
            for i in range(word_width):
                r = coords[start+i][0]
                c = coords[start+i][1]
                if word[word_width-i-1] != grid[r][c][0]:
                    equl = False
                    break

            if equl == True:
                for i in range(word_width):
                    r = coords[start+i][0]
                    c = coords[start+i][1]
                    grid[r][c][1]  = True       
                #print(word)             
                return  True    

def  vertical_find_word(word,grid):

    kk=0
    row_num    = len(grid)
    word_width = len(word)
    if word_width <= row_num:     

        for r in range(0,row_num-word_width+1):
            for c in range(0,len(grid[0])):
                equl = True
                for j in range(word_width):
                    if word[j] != grid[r+j][c][0]:
                        equl=False
                        break
                    else:
                        kk =1
                
                if equl == True:
                    for  k in range(r,r+word_width):
                        grid[k][c][1]  = True
                    return True

        #reverse find
        for r in range(row_num-1,0,-1):   
            if r +1< word_width:
                break
            for c in range(0,len(grid[0])):            
                for j in range(word_width):
                    equl = True
                    if word[j] != grid[r-j][c][0]:
                        equl=False
                        break
                    else:
                        kk =1

                if equl == True:
                    for  k in range(r,r-word_width,-1):
                        grid[k][c][1]  = True
                    return True

    return False


def  horizental_find_word(word,grid):
    
    col_width = len(grid[0])
    word_width = len(word)
    if word_width <= col_width:     

        for r in range(0,len(grid)):
            for c in range(0,col_width-word_width+1):
                equl = True
                for j in range(word_width):
                    if word[j] != grid[r][c+j][0]:
                        equl=False
                        break
                
                if equl == True:
                    for  k in range(c+j,c+j-word_width,-1):
                        grid[r][k][1]  = True
                    return True

            #reverse find
        for r in range(0,len(grid)):            
            for c in range(col_width-1,0,-1):
                if c +1< word_width:
                    break
                for j in range(word_width):
                    equl = True
                    if word[j] != grid[r][c-j][0]:
                        equl=False
                        break
                
                if equl == True:
                    for  k in range(c-j,c-j+word_width):
                        grid[r][k][1]  = True
                    return True

    return False






nums = input().split()
rows= int(nums[0])
cols= int(nums[1])

data = input()
words = input().split()
print("--------------")


grid=[]
index = 0
for r in range(rows):
    col = []
    for c in range(cols):
        col.append( [data[index],False] )
        index +=1
    grid.append(col)


for r in range(rows):
    for c in range(cols):
        print( grid[r][c][0],end=" " )
    print("")        
print("")            


for word in words:
    if  not horizental_find_word(word, grid):
      if  not vertical_find_word(word,grid):
          diagonals_find_word(word,grid)
          



#for r in range(rows):
#    print(grid[r])        
#print(words)

str = ""
for r in range(rows):
    for c in range(cols):
        if not grid[r][c][1] :
            str+= grid[r][c][0]
print(str)

