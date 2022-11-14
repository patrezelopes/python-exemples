'''
Write a Python Function which given a list of integers and number, returns list of all unique pairs which add up to number.
E.g 1) list = [2, 3, 10, 5, 7, 8] number = 15
Output = [(10, 5), (7, 8)]
E.g. 2) list = [7, 10, 2, 21] number = 23
Output = [(2, 21)]
Note: 1) Assume list always has at-least one element
2) List can have both positive or negative elements
'''


def unique_pair(list_int: list, number: int) -> list:
    sum_nums = number

    def remove_repetition(pairs: list) -> list:
        set_pairs = set(pairs)
        set_pairs.remove(None)
        return list(set_pairs)

    def order(num1, num2):
        return (num1, num2) if num1 > num2 else (num2, num1)

    if list_int:
        sum_array = list(map(lambda num: sum_nums - num, list_int))
        pairs = list(map(lambda x: order(x[1], list_int[x[0]]) if x[1] in list_int else None, enumerate(sum_array)))
        return remove_repetition(pairs)


if __name__ == "__main__":
    assert unique_pair([2, 3, 10, 5, 7, 8], 15) in [[(10, 5), (7, 8)], [(8, 7), (10, 5)]]
    assert unique_pair([7, 10, 2, 21], 23) in [[(2, 21)], [(21, 2)]]
    assert unique_pair([-7, -10, -2, 25], 23) in [[(2, 21)], [(25, -2)]]