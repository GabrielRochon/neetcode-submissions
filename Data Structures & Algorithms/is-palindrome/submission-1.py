class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # Classic two pointers problem
        # Pointers at either end of s. when right >= left, return True. Move pointers towards each other.
        # Return False if mismatch. 
        # Complexity: O(n) time, O(1) space.

        # Sanitize string first. Easier that way
        sanitized_list = []
        for char in s:
            if char.isalnum():
                if char.isupper():
                    char = char.lower()
                sanitized_list.append(char)

        print(sanitized_list)

        # Go through list
        left = 0
        right = len(sanitized_list) - 1

        while left < right:
            if sanitized_list[left] != sanitized_list[right]:
                return False
            left += 1
            right -= 1

        return True