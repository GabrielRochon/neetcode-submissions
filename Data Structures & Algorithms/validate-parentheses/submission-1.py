class Solution:
    def isValid(self, s: str) -> bool:
        
        # Typical stack problem
        # Append an open parenthesis. If it doesn't match the top of the stack, then the string is invalid
        # Complexity: O(n) time, O(n) space worse case

        stack = []
        brackets = { '{': '}', '(': ')', '[': ']' }

        for char in s:
            top_pile = stack[-1] if len(stack) >= 1 else None
            if char in brackets.keys():
                stack.append(char)
            elif char not in brackets.keys() and top_pile and brackets[top_pile] == char:
                stack.pop()
            else:
                return False

        return len(stack) == 0
