class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur = defaultdict()
        res = 0
        i = 0

        while i < len(s):
            if s[i] in cur:
                res = max(res, len(cur))
                i = cur[s[i]] + 1
                if (i >= len(s)): break
                cur = defaultdict()
                cur[s[i]] = i
                i += 1
            else:
                cur[s[i]] = i
                i += 1

        res = max(res, len(cur))
        return res