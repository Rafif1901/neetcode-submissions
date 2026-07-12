class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = "".join(char for char in s if char.isalnum()).lower()
        n = len(clean_s)
        l = 0
        r = n-1
        while l<r:
            if clean_s[l] != clean_s[r]:
                return False
                break
            else:
                l+=1
                r-=1
        return True
            
            