class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for anagram in strs: 
            count = [0] * 26 
            for c in anagram:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(anagram)
        
        return list(res.values())

"""
Learned about defaultdict and how to use it to group anagrams together. 
The key is to create a count of characters for each anagram and use that as the key in the dictionary. 
This way, all anagrams will have the same key and will be grouped together in the resulting list.

"""