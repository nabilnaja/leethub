class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        addition = lambda x , y : x + y
        subtraction = lambda x , y : x - y
        division = lambda x , y : int(x / y)
        multiplication = lambda x , y : x * y
        operation = {'+':addition, '-':subtraction, '/':division, '*':multiplication}
        stack = []
        for token in tokens:
            if token in operation:
                sec = int(stack.pop())
                first = int(stack.pop())
                stack.append(operation[token](first,sec))
            else:
                stack.append(token)
        return stack[0]
            