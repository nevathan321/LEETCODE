

# Brute Force Approach O(n^2) time complexity and O(1) space complexity
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):   # ensures j != i and no duplicates
                if nums[i] + nums[j] == target:
                    return [i, j]
                
# Optimal Approach O(n) time complexity and O(n) space complexity
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, j in enumerate(nums): 
            need = target - j 
            if need in seen:
                return [seen[need], i]
            seen[j] = i
