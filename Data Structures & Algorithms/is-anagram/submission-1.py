class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        str1 = [0] * 26
        str2 = [0] * 26

        for i in s:
            str1[ord(i) - ord('a')] += 1
        for i in t:
            str2[ord(i) - ord('a')] += 1
        
        return True if str1 == str2 else False
        