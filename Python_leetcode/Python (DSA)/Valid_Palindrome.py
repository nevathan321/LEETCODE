class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True
    
#--------
# Second Solution

class Solution:
    def isPalindrome(self, s: str) -> bool:
        news = s.replace(" ", "")
        a, b = 0, len(news) - 1
        

        while a < b:
            if news[a].isalnum() and news[b].isalnum():
                if news[a].lower() != news[b].lower():
                    return False
                a += 1
                b -= 1
            elif news[a].isalnum():
                b -= 1
            else:
                a += 1

        return True
