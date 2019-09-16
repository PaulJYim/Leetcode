def isValid(self, s: str) -> bool:
    stack = []

    if not s:
        return True

    for ch in s:
        if(ch == '(' or ch == '{' or ch == '[') :
            stack.append(ch)

        elif(ch == ')'):
            if(stack):
                top = stack.pop()
                if(top != '('):
                    return False
            else:
                return False

        elif(ch == '}'):
            if(stack):
                top = stack.pop()
                if(top != '{'):
                    return False
            else:
                return False

        elif(ch == ']'):
            if(stack):
                top = stack.pop()
                if(top != '['):
                    return False
            else:
                return False

    if(stack):
        return False
    else:
        return True
'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

'''
