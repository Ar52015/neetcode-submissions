class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        pre = [1] * l
        suf = [1] * l

        for i in range(1, l):
            pre[i] = pre[i-1] * nums[i-1]
            suf[l-1-i] = suf[l-i] * nums[l-i]
            
        res = [1] * l

        for i in range(l):
            res[i] = pre[i] * suf[i]

        return res