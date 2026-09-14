class Solution:
    def isValid(self, s: str) -> bool:

        p = []

        for c in s:
            
            if c == '(' or c == '{' or c == '[':
                p.append(c)
            
            if c == ']':
                if len(p) == 0:
                    return False
                elif p.pop() != '[':
                    return False
            if c == ')':
                if len(p) == 0:
                    return False
                elif p.pop() != '(':
                    return False
            if c == '}':
                if len(p) == 0:
                    return False
                elif p.pop() != '{':
                    return False

        return len(p) == 0
                
        