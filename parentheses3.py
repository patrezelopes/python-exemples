import timeit


def parentheses(n, open=0, close=0, s="", answer=None):
    if answer is None:
        answer = []
    if open == close == n and len(s) == n*2:
        answer.append(s)
    if open < n:
        parentheses(n, open + 1, close, s + "(", answer)
    if close < open:
        parentheses(n, open, close + 1, s + ")", answer)
    return answer


if __name__ == '__main__':
    start = timeit.default_timer()
    for i in range(1, 6):
        result = parentheses(i)
        print(result, len(result))
    end = timeit.default_timer()
    print(end - start)
