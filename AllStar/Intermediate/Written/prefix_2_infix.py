def prefix_to_infix(expression):
    stack = []
    for char in reversed(expression):  # 反向遍历前缀表达式
        if char.isalnum():  # 如果是字母或数字，直接入栈
            stack.append(char)
        else:
            operand1 = stack.pop()  # 弹出栈顶元素作为操作数1
            operand2 = stack.pop()  # 弹出栈顶元素作为操作数2
            stack.append(f"({operand1}{char}{operand2})")  # 使用括号将操作数与运算符连接成子表达式，并入栈
    return stack[0]  # 最终栈内剩下的元素即为中缀表达式

prefix_expression = "+-/+A^B2^A2/*ACB**ABC"
infix_expression = prefix_to_infix(prefix_expression)
print("中缀表达式：", infix_expression)
