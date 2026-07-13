class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:    
        res = []

        freqmap = [[] for i in range(len(nums) + 1)]
        counter = {}

        for i in nums:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1

        for v, f in counter.items():
            freqmap[f].append(v)

        for i in range(len(freqmap)-1, -1, -1):
            if freqmap[i] != [] and k != 0:
                for j in freqmap[i]:
                    res.append(j)
                    k -= 1
                    if k == 0:
                        break

        return res