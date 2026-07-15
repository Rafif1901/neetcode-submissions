class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] +=1

        sorted_d = sorted(d.items(), key=lambda item: item[1])
        top_key = sorted_d[-k:]
        return [item[0] for item in top_key]
                