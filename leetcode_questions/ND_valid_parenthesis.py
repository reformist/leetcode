# idea: push on open parenthesis and pop off closed parenthesis. make sure closed matches open. 
# if stack isn't empty at the end, return False (could've been just open parenthesis)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            else:
                if len(stack) == 0: return False
                popped_value = stack.pop()
                if (i == ")" and popped_value != "(") or (i == "}" and popped_value  != "{") or (i == "]" and popped_value  != "["): 
                    return False
        print(len(stack))
        return not stack






