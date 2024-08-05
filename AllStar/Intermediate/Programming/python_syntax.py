'''
输入：
  1.输入整数，并将其转换为列表：    list(map(int, input().split()))

输出：   
  1. 字符串左右对齐并填充特定字符:  str1.ljust(max_length_c2,'-')  or rjust()


字符串:
  1. 用一个或多个空格分割单词:     re.split(r"[ ]+",line1)
                                 params = str.split(":")
  2. 替换/去掉字符串中特定支付：   re.sub(r"[,.;'?!]","",word)
  3. 忽略大小写比较：             str1.lower() == str2.lower()     

正则表达式：
  1. 换意符\的用法:               r'\(\)\[\]'
  2. findall一次找出所有匹配:     matches= re.findall(r'[\(\[][-]?[\d]+,[-]?[\d]+[\)\]]',line)
  3. 特定字符分词：               sentences = re.split(r"[.|?] ",text)
  4. 特定字符串匹配：             matched = re.match(r"[a-zA-Z_]+\w*$", text)





数据结构：
  1. pair的用法:                vals.append( (start,end) )
  2. 二维数组初始化：            array_2d = [[0 for _ in range(cols)] for _ in range(rows)]  or
                                array_2d = [ [0,0,0,0, 1,52,0,0,0,0], [0,0,0,0, 2,51,0,0,0,0]]
  3. 用list实现stack:           numbers.append(5)  numbers.pop()
  4. 用list实现queue:           numbers.append(5)  numbers.pop(0)
  5. 深拷贝:                    import copy    copied = copy.deepcopy(from)

算法：        
  1. 冒泡排序：        
                                n= len(vals)
                                for i in range(n):
                                    for j in range(0,n-i-1):
                                        if vals[j][0] > vals[j+1][0]:
                                            vals[j],vals[j+1]=vals[j+1],vals[j]      

  2. 找出list中字符串的最大长度:   max(len(s) for s in col1)                                        
  3. 数组排序:                    list1.sort()
  4. 数组子集判断：
                                 def all_elements_in_array(array1, array2):
                                    set2 = set(array2)  
                                    for element in array1:
                                        if element not in set2:
                                            return False
                                    return True


语法：
  1. 函数内引用全局变量:
                                def reset(str):
                                    global letters,counter    
'''



#-----------------------------
# 输入整数，并将其转换为列表
#-----------------------------
numbers = list(map(int, input().split()))
player_loc = numbers[:3]
myself_loc = numbers[3:6]

#-----------------------------
# 输入多行参数
#-----------------------------
lines=[]
while True:
    line = input().strip()
    if not line:
        break
    lines.append(line)

for line in lines:
    print(line)



#-----------------------------
#   二维数组
#-----------------------------
rows = 3
cols = 3
array_2d = [[0 for _ in range(cols)] for _ in range(rows)]

for row in array_2d:
    print(row)
array_2d[1][1] = 2

#直接初始化
array_2d = [
            [0,0,0,0, 1,52,0,0,0,0],
            [0,0,0,0, 2,51,0,0,0,0],
            [7 ,6, 5, 4, 3, 50, 49, 48, 47, 46],
            [8 ,9 ,10 ,11 ,12 ,41 ,42 ,43 ,44, 45],
            [17 ,16 ,15 ,14 ,13 ,40 ,39 ,38 ,37 ,36],
            [18 ,19 ,20 ,21 ,22 ,31 ,32 ,33 ,34 ,35],
            [0,0,0,0,23, 30,0,0,0,0],
            [0,0,0,0,24, 29,0,0,0,0],
            [0,0,0,0,25,28,0,0,0,0],
            [0,0,0,0,26, 27,0,0,0,0]
] 

#-----------------------------
#   函数内重设全局变量
#-----------------------------
def reset(str):
    global letters,counter
    letters=[]
    counter=[]

#-----------------------------
#   100以内质数和完全平方数
#-----------------------------
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
sqrn =[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
