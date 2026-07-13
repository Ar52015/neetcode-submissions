class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ht = {}     # index
        res = []

        for i in strs:

            arr = [0] * 26
            for c in i:
                arr[ord(c) - ord('a')] += 1

            tmp = tuple(arr)
            if tmp in ht:
                res[ht[tmp]].append(i)
            else:
                ht[tmp] = len(res)
                res.append([i])

        return res