def is_operator(c):
    return c in ['+', '-', '*', '/']

def prefix_to_postfix(expression):
    stack = []
    expression = expression[::-1]  # Reverse the input expression
    for char in expression:
        if not is_operator(char):
            stack.append(char)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            postfix_exp = operand1 + operand2 + char
            stack.append(postfix_exp)
    return stack.pop()

prefix_expression = "*+ab-cd"
postfix_expression = prefix_to_postfix(prefix_expression)
print("Converted postfix expression:", postfix_expression)
