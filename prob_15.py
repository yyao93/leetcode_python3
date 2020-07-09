class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # hash table
        nums.sort()
        ret = set()
        for i, n in enumerate(nums):
            if n > 0: break
            if i > 0 and nums[i] == nums[i - 1]: continue
            D = {}
            for j in range(i + 1, len(nums)):
                if nums[j] in D:
                    ret.add((n, D[nums[j]], nums[j]))
                else:
                    D[-n - nums[j]] = nums[j]
        return list(map(list, ret))
