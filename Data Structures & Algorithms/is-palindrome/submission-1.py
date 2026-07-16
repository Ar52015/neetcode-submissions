class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(filter(str.isalnum, s))

        l = 0
        r = len(clean) -1

        while (l < r):
            if clean[l].lower() == clean[r].lower():
                l += 1
                r -= 1
            else:
                return False

        return True        