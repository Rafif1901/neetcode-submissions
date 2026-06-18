class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {')':'(', ']':'[', '}':'{'}

        for k in s:
            if k not in close_to_open:
                stack.append(k)
                continue

            if not stack or stack[-1] != close_to_open[k]:
                return False
            
            stack.pop()
        return len(stack) ==0
