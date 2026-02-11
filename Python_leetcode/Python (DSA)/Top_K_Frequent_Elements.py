

# My solution, Time complexity: O(n log n) because of the sorting, Space complexity: O(n) because of the dictionary
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}


        for num in nums:
            dictionary[num] = dictionary.get(num, 0) + 1
        
        sortednums = sorted(dictionary.keys(), key= lambda x: dictionary[x], reverse = True)

        return sortednums[:k]
    
# Neetcode solution, Time complexity: O(n) because we are using a bucket sort, Space complexity: O(n) because of the dictionary and the bucket
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums: 
            count[num] = count.get(num, 0) + 1
        
        for n, c in count.items(): 
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, - 1):
            for n in freq[i]: 
                res.append(n)
                if len(res) == k:
                    return res 