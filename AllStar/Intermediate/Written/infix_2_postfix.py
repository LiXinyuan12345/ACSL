# 定义运算符的优先级
precedence = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3
}

# 将中缀表达式转换为后缀表达式
def infix_to_postfix(expression):
    output = []
    stack = []
    
    for char in expression:
        if char.isalnum():
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and precedence.get(stack[-1], 0) >= precedence.get(char, 0):
                output.append(stack.pop())
            stack.append(char)
    
    while stack:
        output.append(stack.pop())
    
    return ''.join(output)

# 测试转换函数
infix_expression = "((A*(B+C))/2)-(3*A+4)/(A-C)"
postfix_expression = infix_to_postfix(infix_expression)
print("中缀表达式:", infix_expression)
print("后缀表达式:", postfix_expression)
