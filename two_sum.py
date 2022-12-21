class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        return list(map(lambda x: x[0], filter(lambda num: target - num[1] in nums[:num[0]] + nums[num[0]+1:], enumerate(nums))))


if __name__ == '__main__':
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert s.twoSum([3, 2, 4], 6) == [1, 2]
    assert s.twoSum([3, 3], 6) == [0, 1]
