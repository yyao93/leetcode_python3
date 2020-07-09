class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ret = float("inf")  
        for i, n in enumerate(nums[:-2]):
            p1, p2 = i + 1, len(nums) - 1
            while p1 < p2:
                if abs(ret - target) > abs(nums[p2] + nums[p1] + n - target):
                    ret = nums[p2] + nums[p1] + n
                if nums[p1] + nums[p2] + n < target:
                    p1 += 1
                elif nums[p1] + nums[p2] + n > target:
                    p2 -= 1
                else:
                    return target
        return ret
