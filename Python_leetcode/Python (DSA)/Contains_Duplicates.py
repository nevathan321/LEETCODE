class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        listA = []
        for num in nums:
            if num in listA: 
                return True
            listA.append(num)

        return False
