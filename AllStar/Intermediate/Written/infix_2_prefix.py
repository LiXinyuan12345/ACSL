def infix_to_prefix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    prefix = []
    for char in expression[::-1]:
        if char.isalnum():  # 如果是字母或数字，直接放入前缀表达式列表
            prefix.append(char)
        elif char == ')':  # 如果是右括号，入栈
            stack.append(char)
        elif char == '(':
            while stack and stack[-1] != ')':  # 如果是左括号，依次弹出栈内元素至左括号
                prefix.append(stack.pop())
            stack.pop()  # 弹出左括号
        else:
            while stack and precedence.get(stack[-1], 0) > precedence.get(char, 0):  # 如果是运算符，比较优先级
                prefix.append(stack.pop())
            stack.append(char)  # 将当前运算符入栈
    while stack:  # 将栈内剩余元素加入前缀表达式列表
        prefix.append(stack.pop())
        
    return ''.join(prefix[::-1])  # 将前缀表达式列表反转并连接成字符串

infix_expression = "((a+b)^2-c)/(d+e*(b^2-a))"
prefix_expression = infix_to_prefix(infix_expression)
print("中缀表达式:", infix_expression)
print("前缀表达式：", prefix_expression)
