def is_balanced(expression):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in mapping:
            # Check if the current character is a closing bracket
            top_element = stack.pop() if stack else '#'
            # If the stack is not empty, pop the top element; otherwise, use '#'
            
            if mapping[char] != top_element:
                # If the mapping of the current character doesn't match the top element,
                # the expression is not balanced
                return False
        else:
            # If the current character is an opening bracket, push it onto the stack
            stack.append(char)
    
    # The expression is balanced if the stack is empty at the end
    return not stack

expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False
