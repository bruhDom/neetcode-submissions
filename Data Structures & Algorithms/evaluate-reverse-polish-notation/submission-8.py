class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        operations = ["+", "-", "*", "/"]


        for n in tokens:
            if n not in operations: # If we find a number, add it to the stack
                stack.append(n)
            
            else:
                value2 = int(stack.pop())
                value1 = int(stack.pop()) # pop 2 elements on stack and compute result
                result = 0
                if n == "+":
                    result += (value1 + value2)
                    stack.append(result)
                elif n == "-":
                    result += (value1 - value2)
                    stack.append(result)
                elif n == "*":
                    result += (value1 * value2)
                    stack.append(result)
                elif n == "/":
                    result += (value1 / value2)
                    stack.append(result)
        
        
        return int(stack.pop())
