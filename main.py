arr = [19, 20, 21, 22]
#           ^       ^
target_sum = 42


# expected_output = (1, 3)
# https://docs.python.org/3/library/stdtypes.html#list
def find_sum_pair(arr, target_sum):
    first = second = None
    # for index1, num in enumerate(arr):
    #     arr2 = arr.copy()
    #     first = arr2.pop(index1)
    #     for index2, num2 in enumerate(arr2):
    #       if first + num2 == target_sum:
    #           second = num2
    #           return index1, arr.index(second)

    expects = dict()
    for num in arr:
        expects.setdefault(num, target_sum - num)
    print(expects)

print("result: ", find_sum_pair(arr, target_sum))