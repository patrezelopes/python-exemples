import itertools


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        return list(map(lambda x: x[1],
                        filter(lambda num: target - num[1] in nums[:num[0]] + nums[num[0] + 1:], enumerate(nums))))

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        # list(filter(lambda z: sum(z) == 0,
        return list(map(lambda x: (self.twoSum(nums, x), x), nums))
        # ))


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
    assert s.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
