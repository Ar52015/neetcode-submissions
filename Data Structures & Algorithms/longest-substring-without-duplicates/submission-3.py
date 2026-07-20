class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur = defaultdict()
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in cur:
                l = max(cur[s[r]] + 1, l)
            cur[s[r]] = r
            res = max(res, r-l+1)

        return res