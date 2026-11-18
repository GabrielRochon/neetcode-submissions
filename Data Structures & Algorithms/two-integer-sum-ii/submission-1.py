class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # Two pointer problem. Since array is sorted, we can confidently add / remove elements to evaluate
        # ex. [1,2,4,6,10], target = 9
        # We know 10 has no valid partnet to sum to target since sum is 11. So we can confidently delete 10, end -= 1
        # Same principle if sum < target, then the number is too small, so raise it.

        start = 0
        end = len(numbers) - 1

        while start < end:
            sum = numbers[start] + numbers[end]
            if sum > target:
                end -= 1
            elif sum < target:
                start += 1
            else:
                return [ start+1, end+1 ]