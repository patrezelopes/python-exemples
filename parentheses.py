import itertools
import timeit


def valid_parentheses(expr):
    stack = []
    for c in expr:
        if c == '(':
            stack.append(c)
        elif c == ')':
            try:
                stack.pop()
            except IndexError:
                return False
    return len(stack) == 0


def all_permutations(n):
    elements = '(' * n + ')' * n
    return itertools.permutations(elements)


def parentheses(n):
    results = []
    for p in all_permutations(n):
        p = ''.join(p)
        if valid_parentheses(p) and p not in results:
            results.append(p)
    return results


if __name__ == '__main__':
    start = timeit.default_timer()
    for i in range(1, 6):
        result = parentheses(i)
        print(result, len(result))
    end = timeit.default_timer()
    print(end - start)
