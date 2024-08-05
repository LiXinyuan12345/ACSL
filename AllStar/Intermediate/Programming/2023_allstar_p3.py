'''
字符串:
  1. 用一个或多个字符串分割单词:   re.split(r"[ ]+",line1)
  2. 替换/去掉字符串中特定支付：   re.sub(r"[,.;'?!]","",word)
  3. 忽略大小写比较：             str1.lower() == str2.lower() 
  4. 找出list中字符串的最大长度:   max(len(s) for s in col1)

打印格式化：
  1. 字符串左右对齐并填充特定字符:  str1.ljust(max_length_c2,'-')  or rjust()
  

'''
import re

line1 = '''KWIC is an acronym for Key Word In Context, the most common format for concordance lines which is used for  indexing in context.'''
line2 ="for in the"
line3 = "7 15"

#word split 
words = re.split(r"[ ]+",line1)
keywords = re.split(r"[ ]+",line2)
line3    = re.split(r"[ ]+",line3)
line_no =  (int(line3[0]), int(line3[1]))

only_words= []
for word in words:
   newword= re.sub(r"[,.;'?!]","",word)
   stop = (len(newword) != len(word) and  len(word) >0)
   only_words.append( (newword,stop))

#find the col2
col2=[]
for i in range(len(only_words)):
    if only_words[i][0].lower() not in keywords:
        col2.append( (only_words[i][0].lower(),i) )

#sort he col2
n= len(col2)
for i in range(n):
    for j in range(0,n-i-1):
        if col2[j][0] > col2[j+1][0]: 
            col2[j],col2[j+1]=col2[j+1],col2[j]
        elif words[j][0] ==words[j+1][0] and words[j][1] > words[j+1][1] :
            col2[j],col2[j+1]=col2[j+1],col2[j]

#find col1 and col3
col1 = []
col3 = []
for c2 in col2:
    cnt = 3
    strc1 =""
    #backward
    for i in range(c2[1]-1,c2[1]-4,-1):
        if cnt ==0 or i <0:
            break
        if only_words[i][1] or only_words[i][0].lower() in keywords : #stop flag
            break
        strc1 = " "+only_words[i][0] + strc1
        cnt-=1
    if len(strc1)>0 and strc1[0]==' ':
        col1.append(strc1[1:])
    else:
        col1.append(strc1)

    #frontward
    cnt = 3
    strc3=""
    stop  = only_words[c2[1]][1]
    if  not stop: # not stop flag
        for i in range(c2[1]+1,len(only_words)):
            if only_words[i][0].lower() in keywords : #stop flag
                break
            strc3 += only_words[i][0]+" "
            cnt-=1
            if cnt ==0:
                break
        if len(strc3)>0 and strc3[-1]==' ':
            col3.append(strc3[:-1])
        else:
            col3.append(strc3)
    else:
        col3.append("")

#format string
col22=[]
for c2 in col2:
    col22.append( only_words[c2[1]][0])
    
max_length_c1 = max(len(s) for s in col1)
max_length_c2 = max(len(s) for s in col22)
max_length_c3 = max(len(s) for s in col3)

print(max_length_c2,max_length_c3)
print(words)
print("")
print(only_words)
print("")

for i in range(len(col2) ):
    index= col2[i][1]
    c22= only_words[index][0]
    print( col1[i].rjust(max_length_c1,'-'),
           "<"+c22.ljust(max_length_c2,'-')+">",
           col3[i].ljust(max_length_c3,'-'))

