# Author: zzk


def check_brackets(s):
    stack = []
    dic = {")": "(", "]": "[", "}": "{"}
    for char in s:
        if char in {"(", "[", "{"}:
            stack.append(char)
        elif char in dic:
            if len(stack) > 0 and stack[-1] == dic[char]:
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False

print(check_brackets("()[]{([{[}])}"))

