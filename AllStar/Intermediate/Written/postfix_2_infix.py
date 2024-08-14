def postfix_to_infix(expression):
    stack = []
    operators = set(['+', '-', '*', '/'])


    for char in expression:
        if char not in operators:  # 如果是操作数，直接入栈
            stack.append(char)
        else:  # 如果是运算符，弹出栈顶两个操作数，并将运算符与操作数组合成子表达式后入栈
            operand2 = stack.pop()
            operand1 = stack.pop()
            sub_expression = f"({operand1}{char}{operand2})"
            stack.append(sub_expression)
    
    return stack[0]  # 最终栈内剩下的元素即为中缀表达式

postfix_expression = "ABC+*2/3A*4+AC-/-"
infix_expression = postfix_to_infix(postfix_expression)
print("中缀表达式：", infix_expression)
