def is_valid_parentheses(s: str) -> bool:
    """
    Returns True if the input string contains valid parentheses.
    Uses a stack to match opening and closing brackets.
    """
    stack = []

    for ch in s:
        if ch == '(':
            stack.append(')')
        elif ch == '[':
            stack.append(']')
        elif ch == '{':
            stack.append('}')
        elif not stack or ch != stack.pop():
            return False

    return not stack


if __name__ == "__main__":
    print(is_valid_parentheses("()"))        # True
    print(is_valid_parentheses("()[]{}"))    # True
    print(is_valid_parentheses("(]"))        # False
    print(is_valid_parentheses("([)]"))      # False
    print(is_valid_parentheses("{[]}"))      # True