import sys

def count_vowels(string,r):
    vowels = "aeiouAEIOU"  # 包含所有的元音字母（大小写）
    count = 0
    for i in range(len(string)):
        if r[i] == 'G' and string[i] in vowels:
            count += 1
    return count


inputs = input().split()
target = inputs[0]
inputs.pop(0)


result = []
for word in inputs:
    word_match = ['-']*5
    for i in range( 5 ):
        if target[i] == word[i]:
            word_match[i] = 'G'
        
    for i in range( 5 ):
        if word_match[i] != 'G':
            for j in range(5):
                if word[i] == target[j] and word_match[j] != 'G':
                    word_match[i] = 'Y'
                    break
    result.append(''.join(word_match))

#print(inputs)
#print(result)

matched = []
for i in range(len(result)):

    if result[i].count('G') > 0:
        matched.append( (result[i].count('G'), 
                        result[i].count('Y'), 
                        1 if result[i][0]=='G' else 0,
                        1 if result[i][-1]=='G' else 0,
                        count_vowels(inputs[i],result[i]),
                        inputs[i] ,
                        result[i])   ) 

sorted_matched = sorted(matched, key=lambda x: x[0]*10000+x[1]*1000+x[2]*100 + x[3]*10+x[4]) 
sorted_matched.reverse()
#print(matched)         

N = min(6,len(sorted_matched))
sorted_matched= sorted_matched[:N]
if  N >= 6:
    for v in sorted_matched:
        print(v[5],end=' ')   
else:
    str =""
    for i in range( ord('a'),ord('z')+1):
        c = i
        found = False
        for v in inputs:
            if chr(c) in v:
                found= True
                break
        if not found:
            str+= chr(c)   
    print(str)

