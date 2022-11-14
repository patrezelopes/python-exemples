# d = [1, 4, 2, 5, 7, 19, 37]
# d[-1] = [37]
# d[0:6] = [1, 4, 2, 5, 7, 19, 37]
# d[3:5] = [5, 7, 19]
# d[-1:] = [37]
# d[-3:-1] = [7, 19, 37]
# d[::-3] = [1, 4, 2, 5]
# d[::-1] = [1, 4, 2, 5, 7, 19, 37]

_str = "hello"
# convert it to a list of alphabet in reverse order
# and convert it to Capital Letter.
# Like ["O", "L", "L", "E", "H"]

# reverse = [_str[i].capitalize() for i in range(len(_str) - 1, -1, -1)]
# print(reverse)


# def my_name_is(func):
#     def wrapper_func(*args, **kwargs):
#         print(f"my name is {func(*args, **kwargs)}")
#     return wrapper_func
#
#
# @my_name_is
# def get_name(name: str) -> str:
#     pass
#
#
# get_name("Patreze")


# list_nums = list(map(lambda x: x*x, range(10)))
# print(list_nums)
#
#
#

list_hello = ["E", "H", "L", "E", "H"]
list_hello.sort(reverse=True)
new_list = list_hello.copy()
print(list_hello)


class DefaultModel(models.Models):
    created_at =
    updated_at =



class Employ(DefaultModel):
    name = models.CH