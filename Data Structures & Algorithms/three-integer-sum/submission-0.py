class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        # Brute-force: compare all triplets. O(n^3), extremely inefficient

        # Optimized approach:
        # 1. Put all numbers in a sec for O(1) checks for existence,
        # 2. Compare all duos, build a dict with key = local sum and values = the 2 numbers
        # As you build the dict, check if entry -key exists (check is O(1)). If it does, you have your 3sum.
        # Time complexity is O(n^2), significantly better

        # Even more optimized: two pointers (Leetcode solution)
        # Sorting is O(nlogn) in most cases. We expect this to be O(n^2) either way so can sort with no consequence on complexity.

        nums = sorted(nums)
        triplets_dict = {}
        answer = []

        for i, num in enumerate(nums):

            j = i+1
            k = len(nums) - 1

            while j < k:

                local_sum = nums[i] + nums[j] + nums[k]

                if local_sum == 0:
                    triplet = sorted([nums[i], nums[j], nums[k]])
                    triplet_key = (triplet[0], triplet[1], triplet[2])
                    if triplet_key not in triplets_dict:
                        triplets_dict[triplet_key] = triplet
                        answer.append(triplet)
                    j += 1
                elif local_sum < 0:
                    j += 1
                else:
                    k -= 1

        return answer