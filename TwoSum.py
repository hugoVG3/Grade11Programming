class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_to_index = {}  # hashmap to store number and its index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i
solver = Solution()
nums1 = [2,7,11,15]
target1=9
result = solver.twoSum(nums1, target1)
print(f"Input: nums = {nums1}, target = {target1}")
print(f"Output: {result}") 