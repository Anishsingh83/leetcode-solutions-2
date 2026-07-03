class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        writer = 0
        reader = 1

        for reader in range(1, len(nums)):
            if nums[reader] == nums[writer]:
                pass
            else:
                writer += 1
                nums[writer] = nums[reader]
        return writer + 1        
