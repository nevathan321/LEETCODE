

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


#--- 
# Did this for fun :)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        seen = []

        for i, num in enumerate(numbers): 
            for j, s in enumerate(seen): 
                if s + num == target: 
                    return [j + 1, i + 1]
            seen.append(num)


#-- 
# the standard approach for this now :(

def twoSum(numbers: List[int], target: int) -> List[int]:
    seen = {}

    for i, num in enumerate(numbers): 
        need = target - num 
        if need in seen: 
            return [seen[need] + 1, i + 1]
        seen[num] = i