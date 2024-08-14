def is_operator(c):
    return c in ['+', '-', '*', '/','^']

def postfix_to_prefix(expression):
    stack = []
    for char in expression:
        if not is_operator(char):
            stack.append(char)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            prefix_exp = char + operand1 + operand2
            stack.append(prefix_exp)
    return stack.pop()

postfix_expression = "ab+c*"
prefix_expression = postfix_to_prefix(postfix_expression)
print("Converted prefix expression:", prefix_expression)