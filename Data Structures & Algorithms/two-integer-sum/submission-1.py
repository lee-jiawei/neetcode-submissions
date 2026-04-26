class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}

        for i, v in enumerate(nums):
            dict[v] = i

        for i, v in enumerate(nums):
            diff = target - v
            if diff in dict and dict[diff] != i:
                return [i, dict[diff]]
        return []

# Hash Map (Two Pass) solution