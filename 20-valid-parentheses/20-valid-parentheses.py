class Solution:
    def isValid(self, s: str) -> bool:
        p_mapping = {')':'(','}':'{',']':'['}
        print(s)
        if not s: 
            return True
        if s[0] in p_mapping:
            return False
        stack = []
        for char in s:
            if char in p_mapping:
                if stack[-1] != p_mapping[char] if stack else '#' :
                    return False
                stack.pop()
            else: 
                stack.append(char)
        return not stack
            
        