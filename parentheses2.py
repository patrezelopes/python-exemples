import itertools
import re
import timeit


def parentheses(n):
    elements = '(' * n + ')' * n
    results = list(map(lambda s: ''.join(s),
                       list(filter(lambda p: ''.join(p) if not list(filter(
                           lambda x: len(re.findall('\(', ''.join(p)[:x])) < len(re.findall('\)', ''.join(p)[:x])),
                           range(len(''.join(p))))) else "",
                                   set(itertools.permutations(elements))))))
    return results


if __name__ == '__main__':
    start = timeit.default_timer()
    for i in range(1, 6):
        result = parentheses(i)
        print(result, len(result))
    end = timeit.default_timer()
    print(end - start)

