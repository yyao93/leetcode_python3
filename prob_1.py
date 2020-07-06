def twoSum(nums, target):
    memo = {}
    for i, n in enumerate(nums):
        if n in memo:
            return [memo[n], i]
        memo[target - n] = i

nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))
