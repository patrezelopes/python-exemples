def rotate(nums: list, k: int):
    result = nums[-k:] + nums[:-k]
    return result


if __name__ == '__main__':
    rotate([1, 2, 3], 2)

assert rotate([1, 2, 3, 4, 5, 6], 1) == [6, 1, 2, 3, 4, 5]
assert rotate([1, 2, 3, 4, 5, 6], 2) == [5, 6, 1, 2, 3, 4]
assert rotate([1, 2, 3, 4, 5, 6], 3) == [4, 5, 6, 1, 2, 3]
assert rotate([1, 2, 3, 4, 5, 6], 4) == [3, 4, 5, 6, 1, 2]
