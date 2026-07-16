class Solution:

    def binary_search(self, nums: List[int], l: int, r: int, target) -> int:
        if (l == r):
            if nums[l] == target:
                return l
            else:
                return -1
        elif (l + 1 == r):
            if nums[r] == target:
                return r
            elif nums[l] == target:
                return l
            else:
                return -1
        else:
            if nums[(l+r)//2] == target:
                return (l+r)//2
            elif nums[(l+r)//2] > target:
                temp = self.binary_search(nums, l, (l+r)//2, target)
                return temp
            else:
                temp = self.binary_search(nums, (l+r)//2, r, target)
                return temp


    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        res = self.binary_search(nums, l, r, target)
        return res
