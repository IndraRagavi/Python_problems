from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_uniq = set(nums)
        print(len(nums),len(nums_uniq))
        if len(nums) == len(nums_uniq):
            return False
        else:
            return True


dup = Solution()
print(dup.hasDuplicate([1,2,3,3]))