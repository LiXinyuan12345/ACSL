import re
'''
正则表达式：
  1. 换意符\的用法
  2. findall一次找出所有匹配
  3. 支持多个连续空格的分词:  words = re.split(r'\s+',str)

pair的用法:   元组()

算法：        冒泡排序
'''
# parse data
def line_2_ranges(line):

  vals=[] 
  matches= re.findall(r'[\(\[][-]?[\d]+,[-]?[\d]+[\)\]]',line)
  for range1 in matches:
      str= range1[1:-1]
      str_range = re.split(",",str)

      start = int(str_range[0])
      end   = int(str_range[1])
      if range1[0] == '(':
          start +=1
      if range1[-1]== ")":
          end -=1
          
      vals.append( (start,end) )
  
  # bubble sort  
  n= len(vals)
  for i in range(n):
      for j in range(0,n-i-1):
          if vals[j][0] > vals[j+1][0]:
              vals[j],vals[j+1]=vals[j+1],vals[j]
  return vals


#calc
def pass2(param_lines,min_v,max_v):
    
      sum =0
      for v in range(min_v,max_v+1):
            hit = 0
            for line in param_lines:
                for  rng in line:
                    if rng[0] <= v <= rng[1]:
                        hit+=1
                        break
            if hit==1:
                sum += v

      return sum
      
def pass3(param_lines,min_v,max_v):

      sum1 =0
      sum2 = 0
      for v in range(min_v,max_v+1):
            hit = 0
            for line in param_lines:
                for  rng in line:
                    if rng[0] <= v <= rng[1]:
                        hit+=1
                        break
            if hit==1:
                sum1 += v
            if hit==2:
                sum2 += v

      return sum1,sum2  
          
lines=["(5,10) (-5,2] [24,28][12,22)",
       "[1,4] [15,25) [-4,-1) (7,12]",
       "null"]



lines=[
"[0,5) (-15,-5] [8,12] (-4,0)",
"[3,7) (8,15) [-10,-4) [-4,2] [15,20)",
"null"  
]

lines=[
 "(5,10] [24,25) [13,20] (0,4)",
 "[1,5) [25,26] (8,12] (15,24)",
 "[4,12] [-5,3) (12,25]",
]

lines=[
  "(-84,-80) (-65,-60] [-99,-90) [-80,-70]",
"(-71,-64) [-95,-91) [-74,-71] (-87,-81]",
"[-85,-79) (-71,-62] [-97,-87] (-61,-55)"]

lines=[
"(2,6) (13,17) (6,9) (9,13) (0,2)",
"[15,18] [0,5] [6,14]",
"(11,14] [3,4) (6,10] [5,5]"
]

lines=[]
lines.append(input())
lines.append(input())
str = input()
if str != 'null':
  lines.append(str)

line_ranges=[]
min_v=10000000000
max_v=-10000000000
for line in lines:
   if line != 'null':
      ranges = line_2_ranges(line)
      if len(ranges)> 0:
            if min_v > ranges[0][0]:
                  min_v = ranges[0][0]
            if max_v < ranges[-1][1]:
                  max_v = ranges[-1][1]
            line_ranges.append(ranges)

if len(line_ranges) == 2:
    print(pass2(line_ranges, min_v,max_v))
if len(line_ranges)==3:
    sum1,sum2 = pass3(line_ranges, min_v,max_v)
    print(sum1,sum2)

