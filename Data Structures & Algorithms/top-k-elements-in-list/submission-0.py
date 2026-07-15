class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqCounts = Counter(nums)
        topFreq = freqCounts.most_common(k)
        keys = [num for num, count in topFreq]
        return keys