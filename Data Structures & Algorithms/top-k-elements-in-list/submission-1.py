class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] +=1

        sorted_dict = dict(sorted(d.items(), key=lambda item: item[1]))
        top_key = list(sorted_dict)[-k:]
        return top_key
                