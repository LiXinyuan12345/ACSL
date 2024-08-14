'''
问题：给定一个单词词典和一个句子结构，你将使用词典中的单词生成该结构的句子。

单词词典是一组字符串。每个字符串以表示词性的大写字母开头,后面是单词列表。词类有名词N、命令C、动词V、形容词J、副词B和介词P。
每个单词仅由小写字母组成,单词之间用一个空格隔开。由于英语中只有3篇文章(“a”、“an”和“the”),我们不会将其纳入词典,
但我们会对“a”或“an”中的任何一个使用a(a),对“the”一词使用a(T)。如果下一个单词以元音(a,e,i,o,u)开头,
则使用“an”,否则使用“a”。

句子的类型有：
陈述句(D)用于陈述信息。陈述句以句号结尾。
祈使句(I)发出命令。祈使句以句号结尾。
疑问句 (Q)问问题。因此，它们以问号结尾。它们总是以“什么”开头。
感叹句(E)表达情感，以感叹号结尾。

句子结构是识别上述句子类型的大写字母串，后面是每个句子中每个单词的词性代码。当使用词典中的单词时，当单词列表用尽时，绕着周围再次使用该词性的第一个单词。通过用一个空格分隔每个句子，可以生成多个句子。生成的所有句子都必须以大写字母开头。

For example, assume you are given the following input:
6
B productively
J green
N apple tree birds
C pick
V grows fly
P on above below among
ETJNVBPTN QNVP DTJNVPAJNPN ICAN

This would produce the following output:
The green apple grows productively on the tree! What birds fly above? The green apple grows
below a green tree among birds. Pick an apple.
'''

def get_word(dict,flag):

    if    flag == 'T':   return "the"
    elif  flag == 'A':   return "a"

    word = ""
    for s in dict:
         if s[0] == flag:
             pos = s[2]
             word = s[1][pos] 
             s[2] = (pos+1) % len(s[1])
             break
         
    return word
      

line_num = int(input())
lines = []
for i in range(line_num):
    words =  input().split()
    lines.append( [words[0], words[1:],0] )
sentences = input().split()

result=""
for s in sentences:
    stype = s[0]
    sflag = s[1:]

    end=" "
    words = ""
    if   stype == 'D' or stype == 'I':
         end=". "
    elif stype == 'Q':
         end="? "
         words="what "
    elif stype == 'E':
         end="! "


    a_flag = False
    for flag in sflag:
      word = get_word(lines,flag)
      if  a_flag == True:
            a_flag = False
            if len(word)>0 and word[0] in "aeiouAEIOU":
                words+="n "
            else:
                words+=" "                   

      a_flag = (flag == 'A')
      if not a_flag:
        words += word + " " 
      else:
        words += word
    if len(words)>0 and words[-1]==' ':
        words = words[0:-1] 
    words+= end 

    result += words[0].upper()
    result += words[1:]

if result[-1]==' ':
    result = result[0:-1]
print(result)
'''
单词词典是一组字符串。每个字符串以表示词性的大写字母开头,后面是单词列表。词类有名词N、命令C、动词V、形容词J、副词B和介词P。
每个单词仅由小写字母组成,单词之间用一个空格隔开。由于英语中只有3篇文章(“a”、“an”和“the”),我们不会将其纳入词典,
但我们会对“a”或“an”中的任何一个使用a(a),对“the”一词使用a(T)。如果下一个单词以元音(a,e,i,o,u)开头,
则使用“an”,否则使用“a”。
'''
#print(line_num)
#print(lines)
#print(sentences)



