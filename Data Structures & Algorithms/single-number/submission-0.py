class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashMap = {}
        for i in nums:
            if i in hashMap:
                hashMap[i] +=1
            else:
                hashMap[i] = 1
        
        for n in hashMap:
            if hashMap[n]==1:
                return n