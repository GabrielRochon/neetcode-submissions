class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # Typical binary search

        left = 0
        right = len(nums) - 1

        # Edge cases
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        while left <= right:
            middle = (left + right) // 2

            print(left, middle, right)

            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle+1
            else:
                right = middle-1

        return -1