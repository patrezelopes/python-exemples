import re


def parentheses(k: int):
    result = ["" for _ in range(k)]
    while list(filter(lambda u: len(u) < 2*k, result)):
        result = list(
            map(lambda x: x[1]+''.join(list(
            map(lambda y: "(" if len(x[1]) < 2*k else "", range(x[0]+1)))), enumerate(result)))
        result = list(
            map(lambda z: z[1]+''.join(list(
            map(lambda w: ")", range(len(re.findall('\(', z[1])) - len(re.findall('\)', z[1])))))), enumerate(result)))
    return result


if __name__ == '__main__':
    print(parentheses(1))
    print(parentheses(2))
    print(parentheses(3))

assert set(parentheses(1)) == set(["()"])
assert set(parentheses(2)) == set(["(())", "()()"])
assert set(parentheses(3)) == set(["((()))", "(())(())", "()()()"])
